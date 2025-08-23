"""
Assignment 4: AI-Powered Onboarding System

This solution demonstrates how to create an intelligent onboarding system
that personalizes the user experience using AI agents.
"""

import asyncio
from crewai import Agent, Crew, Task, Process
from crewai.tools import BaseTool
from pydantic import Field, BaseModel
from typing import Type
import re


class EmailGeneratorInput(BaseModel):
    fullname: str = Field(..., description="The full name of the employee.")
    department: str = Field(..., description="The department of the employee.")


# --- Custom Tool Definition ---
class EmailGeneratorTool(BaseTool):
    name: str = "Email Generator"
    description: str = (
        "Generates a company email based on the employee's full name and department."
    )
    args_schema: Type[BaseModel] = EmailGeneratorInput

    def _run(self, fullname: str, department: str) -> str:
        """Generate a company email from fullname and department."""
        name_part = re.sub(r"[^a-zA-Z]", "", fullname.replace(" ", ".")).lower()
        department_part = department.replace(" ", "").lower()
        return f"{name_part}@{department_part}.company.com"


scheduler_agent = Agent(
    role="Scheduler",
    goal="Validate and confirm employee start date",
    backstory="Ensures the selected start date is valid and not a holiday.",
)

it_agent = Agent(
    role="IT Administrator",
    goal="Set up company email and provide PC setup instructions",
    backstory="Prepares company email accounts and delivers simple PC setup guidelines.",
    tools=[EmailGeneratorTool()],
)

report_agent = Agent(
    role="Onboarding Reporter",
    goal="Generate an onboarding summary report",
    backstory="Creates a final onboarding report with all key details for HR records.",
)


validate_start_date_task = Task(
    description=(
        "Check if the start date ({employe}) is a working day. "
        "If it's a holiday or weekend, suggest the next available working day."
    ),
    expected_output="Confirmed valid start date or suggestion for a new date.",
    agent=scheduler_agent,
)

it_setup_task = Task(
    description=(
        "Create a company email for {employe} in the {employe} department. "
        "Provide a short, clear set of bullet points on how to set up their PC."
    ),
    expected_output="Active company email and clear PC setup instructions.",
    agent=it_agent,
)

generate_report_task = Task(
    description=(
        "Generate a summary onboarding report for {employe}, starting on {employe}, "
        "in the {employe} department. Include email details, PC setup info, and start date confirmation."
    ),
    expected_output="A clear and concise onboarding summary report.",
    agent=report_agent,
)

# --- Crew Definition ---
onboarding_crew = Crew(
    agents=[scheduler_agent, it_agent, report_agent],
    tasks=[validate_start_date_task, it_setup_task, generate_report_task],
    process=Process.sequential,
    verbose=True,
)


async def async_onboarding_execution(onboarding_inputs):
    results = await onboarding_crew.kickoff_async(inputs=onboarding_inputs)
    print("Crew result:", results.raw)


onboarding_inputs = {
    "employe": [
        "Alice Johnson, starting 2024-07-15, department Engineering",
        "Bob Smith, starting 2024-07-16, department Marketing",
        "Charlie Brown, starting 2024-07-17, department Sales",
    ]
}


if __name__ == "__main__":
    # Run asynchronous onboarding workflows
    asyncio.run(async_onboarding_execution(onboarding_inputs))
