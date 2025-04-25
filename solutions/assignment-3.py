"""
Assignment 3: Fraud Detection Workflow

This solution demonstrates how to create an AI system that analyzes and
classifies transactions to identify potential fraudulent activities.
"""

from typing import List
from crewai import Agent, Crew, Task
from pydantic import BaseModel
from crewai.tasks.conditional_task import ConditionalTask
from crewai.tasks.task_output import TaskOutput


# Condition to check if anomalies exceed a threshold
def is_escalation_needed(output: TaskOutput) -> bool:
    return len(output.pydantic.anomalies) > 5


class FraudDetectionTaskOutput(BaseModel):
    anomalies: List[str]


# Define Agents
fraud_analyst = Agent(
    role="Fraud Analyst",
    goal="Analyze transactions to detect anomalies",
    backstory="Experienced in financial fraud detection.",
)

escalation_specialist = Agent(
    role="Escalation Specialist",
    goal="Manually review flagged transactions",
    backstory="Handles complex fraud cases requiring human oversight.",
)

report_generator = Agent(
    role="Report Generator",
    goal="Prepare a summary fraud detection report",
    backstory="Compiles findings into actionable insights.",
)


# Function to create tasks using transactions
def create_transaction_tasks(transactions: List[str]):
    task1 = Task(
        description=f"Analyze the following transactions for anomalies: {transactions}",
        agent=fraud_analyst,
        expected_output=f"Number of anomalies detected for each transaction.",
        output_pydantic=FraudDetectionTaskOutput,
    )
    return [task1]


# Define remaining tasks outside the function
conditional_task = ConditionalTask(
    description="Escalate flagged transactions if more than 5 anomalies are detected.",
    agent=escalation_specialist,
    condition=is_escalation_needed,
    expected_output="Validated flagged transactions after manual review.",
)

task3 = Task(
    description="Generate a summary report on fraud detection results.",
    agent=report_generator,
    expected_output="A detailed fraud detection report.",
)

# Define Crew with Manager Agent
manager_agent = Agent(
    role="Fraud Detection Manager",
    goal="Oversee the fraud detection workflow",
    backstory="Ensures efficient fraud analysis and resolution.",
)

# Sample transaction list input
transaction_list = [
    # Normal Transactions
    "TXN1 | Withdrawal | $500 | ATM | New York | 2024-07-01 14:23 | Card Ending: 1234",
    "TXN2 | Online Purchase | $200 | Electronics Store | San Francisco | 2024-07-02 09:45 | IP: 192.168.0.1",
    "TXN3 | Transfer | $1,000 | Bank Account | Zurich | 2024-07-02 17:10 | Beneficiary: John Doe",
    "TXN4 | POS Purchase | $50 | Grocery Store | Berlin | 2024-07-03 12:30 | Card Ending: 5678",
    "TXN5 | Withdrawal | $400 | ATM | Dubai | 2024-07-04 08:15 | Card Ending: 1234",
    "TXN6 | Online Purchase | $150 | Retail Store | Paris | 2024-07-04 20:50 | IP: 10.0.0.2",
    "TXN7 | Transfer | $2,000 | Bank Account | London | 2024-07-05 11:30 | Beneficiary: Jane Smith",
    "TXN8 | POS Purchase | $30 | Coffee Shop | New York | 2024-07-05 15:00 | Card Ending: 5678",
    "TXN9 | Withdrawal | $200 | ATM | San Francisco | 2024-07-06 10:00 | Card Ending: 1234",
    "TXN10 | Online Purchase | $300 | Bookstore | Berlin | 2024-07-06 13:45 | IP: 10.0.0.5",
    # Anomalies
    "TXN11 | Withdrawal | $9,999 | ATM | Las Vegas | 2024-07-07 03:15 | Card Ending: 9999",  # High Amount, Odd Time
    "TXN12 | Transfer | $50,000 | Offshore Account | Cayman Islands | 2024-07-07 05:00 | Beneficiary: Unknown",  # Offshore Account
    "TXN13 | Online Purchase | $5,500 | Luxury Retailer | Unknown Location | 2024-07-07 23:59 | IP: 255.255.255.0",  # Suspicious IP and Location
    "TXN14 | Withdrawal | $7,000 | ATM | Dubai | 2024-07-08 02:30 | Card Ending: 0000",  # Odd Time, High Amount
    "TXN15 | POS Purchase | $1 | Jewelry Store | New York | 2024-07-08 14:00 | Card Ending: 5678",  # Unusually Low Amount
    "TXN16 | Online Purchase | $10,000 | Electronics | Hong Kong | 2024-07-08 22:45 | IP: 192.0.2.1",  # Large Online Purchase
    "TXN17 | Transfer | $25,000 | Bank Account | Zurich | 2024-07-09 16:10 | Beneficiary: Suspicious Entity",  # High Value Transfer
    "TXN18 | Withdrawal | $6,000 | ATM | Remote Location | 2024-07-09 04:45 | Card Ending: 8888",  # Remote Location, Odd Time
    "TXN19 | POS Purchase | $9,000 | Luxury Boutique | Paris | 2024-07-09 19:30 | Card Ending: 1234",  # Unusually High POS Purchase
    "TXN20 | Online Purchase | $8,200 | Unknown Store | Unknown | 2024-07-09 21:15 | IP: 0.0.0.0",  # Untraceable IP, Unknown Store
]


# Create tasks dynamically with transaction input
tasks = create_transaction_tasks(transaction_list) + [conditional_task, task3]

# Initialize Crew
crew = Crew(
    agents=[fraud_analyst, escalation_specialist, report_generator],
    tasks=tasks,
    manager_agent=manager_agent,
    planning=True,
    verbose=True,
)

if __name__ == "__main__":
    # Run the Crew
    result = crew.kickoff()
    print("Fraud Detection Result:", result)
