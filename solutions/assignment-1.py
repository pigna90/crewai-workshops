
"""
Assignment 1: Your First Agent

This solution demonstrates how to create a multi-agent AI application that focuses on
prompt engineering and optimization using CrewAI.
"""

from crewai import Agent, Task, Crew, Process


# Create the Prompt Structure Agent
prompt_structure_agent = Agent(
    role="Prompt Structure Expert",
    goal="Improve the structure, clarity, and completeness of input prompts",
    backstory="""You are an expert in prompt engineering with years of experience
    in crafting clear and effective prompts. You know how to structure prompts
    to get the best results from AI models.""",
    verbose=True,
)

# Create the LLM Optimization Agent
llm_optimization_agent = Agent(
    role="LLM Optimization Specialist",
    goal="Optimize prompts for specific LLM models",
    backstory="""You are a specialist in optimizing prompts for different LLM models.
    You understand the strengths and limitations of various models and know how to
    tailor prompts to get the best results from each one.""",
    verbose=True,
)


def get_crew(prompt: str, target_model: str) -> Crew:
    """
    Enhance and optimize a prompt using a two-agent system.

    Args:
        prompt (str): The original prompt to enhance and optimize
        target_model (str): The target LLM model to optimize for

    Returns:
        str: The enhanced and optimized prompt
    """
    # Define the tasks
    structure_task = Task(
        description=f"""Improve the structure and clarity of this prompt:
        {prompt}
        
        Make it more descriptive, clear, and complete while maintaining its original intent.
        Focus on:
        1. Clear instructions
        2. Proper context
        3. Specific requirements
        4. Expected output format""",
        agent=prompt_structure_agent,
        expected_output="An enhanced version of the prompt with improved structure and clarity.",
    )

    optimization_task = Task(
        description=f"""Optimize the enhanced prompt for the {target_model} model:
        
        Consider:
        1. Model's capabilities and limitations
        2. Best practices for the specific model
        3. Token efficiency
        4. Response quality optimization""",
        agent=llm_optimization_agent,
        expected_output="A final optimized prompt ready for use with the target model.",
    )

    # Create the crew
    crew = Crew(
        agents=[prompt_structure_agent, llm_optimization_agent],
        tasks=[structure_task, optimization_task],
        process=Process.sequential,
        verbose=True,
    )

    return crew


def main():
    """
    Main function to demonstrate the prompt enhancement and optimization system.
    """
    # Example usage
    result = get_crew(
        prompt="Write a story about a robot", target_model="gpt-4"
    ).kickoff()

    print(result)              # shows the overall structured output
    print(result.tasks_output) # lets you see task-by-task outputs

    #output1 = task.execute()
    #print(output1)   # inspect before moving on
    #output2 = task2.execute(inputs=output1)

    print("\nFinal Optimized Prompt:")
    print(result)


if __name__ == "__main__":
    main()
