"""
Assignment 2: Content Creation with Guardrails

This solution demonstrates how to create an AI system that generates content
while ensuring it adheres to safety guidelines using CrewAI Flow.
"""

from crewai import Agent, Task, Crew, Process
from pydantic import BaseModel, Field
from typing import List, Optional
from crewai.flow.flow import Flow, start, listen, router


class ContentState(BaseModel):
    """State management for the content creation process."""

    content: str = ""
    is_safe: bool = False
    generation_attempts_left: int = 2


class ContentCreationFlow(Flow[ContentState]):
    """Flow for creating and validating content with safety guardrails."""

    topic: str = Field(description="Topic for content creation")
    target_platform: str = Field(description="Platform where content will be published")

    def __init__(self, topic: str, target_platform: str):
        super().__init__()
        self.topic = topic
        self.target_platform = target_platform

    @start("retry")
    def generate_content(self):
        """Generate initial content based on the topic."""
        content_creator = Agent(
            role="Content Creator",
            goal="Create engaging and appropriate content",
            backstory="""You are an expert content creator with years of experience
            in creating engaging and appropriate content for various platforms.""",
            verbose=True,
        )

        task = Task(
            description=f"""Create content about {self.topic} for {self.target_platform}.
            The content should be engaging and appropriate for the platform.""",
            agent=content_creator,
            expected_output="A well-written piece of content ready for safety review.",
        )

        crew = Crew(agents=[content_creator], tasks=[task])
        result = crew.kickoff()
        self.state.content = result.raw
        print("Content generated!")

    @listen(generate_content)
    def validate_content(self):
        """Validate the content for safety and appropriateness."""
        print("Validating content...")
        safety_moderator = Agent(
            role="Safety Moderator",
            goal="Ensure content is safe and appropriate",
            backstory="""You are a safety expert who ensures all content
            meets platform guidelines and community standards.""",
            verbose=True,
        )

        task = Task(
            description=f"""Review this content for safety and appropriateness:
            {self.state.content}
            
            Check for:
            1. Violence or harmful content
            2. Inappropriate language
            3. Hate speech
            4. Platform-specific guidelines""",
            agent=safety_moderator,
            expected_output="A safety assessment of the content.",
        )

        crew = Crew(agents=[safety_moderator], tasks=[task])
        result = crew.kickoff()
        self.state.is_safe = "safe" in result.raw.lower()
        print("Content validation complete!")

    @router(validate_content)
    def route_content(self):
        """Route content based on validation results."""
        if self.state.is_safe:
            return "approved"
        elif self.state.generation_attempts_left == 0:
            return "rejected"
        else:
            self.state.generation_attempts_left -= 1
            return "retry"

    @listen("approved")
    def finalize_content(self):
        """Save approved content to a file."""
        with open("approved_content.txt", "w") as file:
            file.write(self.state.content)
        print("Content saved to approved_content.txt")

    @listen("rejected")
    def notify_rejection(self):
        """Handle rejected content."""
        print("Content could not be generated safely after multiple attempts.")


def main():
    """
    Main function to demonstrate the content creation with guardrails system.
    """
    # Example usage
    flow = ContentCreationFlow(
        topic="The benefits of AI in healthcare", target_platform="LinkedIn"
    )
    flow.kickoff()


if __name__ == "__main__":
    main()
