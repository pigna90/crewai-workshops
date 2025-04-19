# Workshop Solutions

This directory contains the Python solutions for the workshop assignments. Each solution is in its own Python file.

## File Structure

```
solutions/
├── README.md
├── requirements.txt
├── assignment-1.py    # Solution for "Your First Agent"
├── assignment-2.py    # Solution for "Content Creation with Guardrails"
├── assignment-3.py    # Solution for "Fraud Detection Workflow"
└── assignment-4.py    # Solution for "AI-Powered Onboarding System"
```

## Requirements

All solutions share the same requirements:
- Python 3.8+
- CrewAI
- OpenAI API key
- SerperDev API key

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   ```bash
   # On macOS/Linux
   export OPENAI_API_KEY='your-key'
   export SERPER_API_KEY='your-key'
   
   # On Windows
   set OPENAI_API_KEY=your-key
   set SERPER_API_KEY=your-key
   ```

## Running the Solutions

To run a specific solution:
```bash
python assignment-1.py  # For the first assignment
python assignment-2.py  # For the second assignment
# and so on...
```

## Note

These solutions are provided as reference implementations. It's recommended to try solving the assignments on your own before looking at the solutions. 