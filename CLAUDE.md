# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a CrewAI workshops repository containing interactive web-based learning materials for Agentic AI and multi-agent application development. The current workshop focuses on Porto Tech Hub 2025.

**Key Architecture**: Branch-based workshop versioning where each workshop version is maintained in its own branch (main = current workshop).

## Repository Structure

- `assignments/` - HTML pages for each workshop assignment
- `solutions/` - Python solutions using CrewAI framework
- `assets/` - Frontend resources (CSS, JS)
- `public/` - Static assets (videos, PDFs, images)
- `index.html` - Main landing page

## Common Development Commands

### Python Solutions Development
```bash
# Navigate to solutions directory
cd solutions

# Install dependencies (uses Poetry/uv)
uv sync

# Set required API keys
export OPENAI_API_KEY='your-key'
export SERPER_API_KEY='your-key'

# Run specific assignment
uv run python assignment-1.py
uv run python assignment-2.py
# etc.
```

### Frontend Development
No build process required - pure HTML/CSS/JS. Simply open `index.html` in browser for local viewing.

## Technology Stack & Key Dependencies

**Frontend**: HTML5, CSS3, Vanilla JavaScript, Font Awesome, Prism.js
**Backend**: Python ^3.10 <3.13, CrewAI 0.114.0 (version locked), Pydantic

**Critical**: CrewAI is locked to version 0.114.0 for compatibility. Python must be >=3.10 and <3.13.

## Architecture Patterns

### CrewAI Multi-Agent System
- **Agent**: Individual AI agents with roles, goals, backstories
- **Task**: Work items assigned to agents
- **Crew**: Orchestration of multiple agents
- **Flow**: State-based workflow management with Pydantic models
- **ConditionalTask**: Decision-based task routing

### Progressive Learning Path
1. Assignment 1: Basic agents and crews (sequential processing)
2. Assignment 2: Flow-based architecture with state management
3. Assignment 3: Conditional tasks with threshold-based routing
4. Assignment 4: Custom tools and async operations
5. Assignment 5: Full-stack production application with Streamlit

### Custom Tool Development
- Inherit from `BaseTool`
- Use Pydantic for input validation
- Support both sync and async execution

## Solution File Structure
Each `assignment-N.py` file is self-contained and follows this pattern:
- Module-level docstring explaining the assignment
- Agent definitions with clear roles and backstories
- Task definitions with expected outputs
- Crew orchestration with verbose mode enabled
- Main execution block

## Branch Strategy
- `main`: Current workshop (Porto Tech Hub 2025)
- `pycon_de_2025`: PyCon DE workshop materials
- `data-hack-summit-2025`: Data Hack Summit materials
- `solutions-data-hack-2025`: Solutions branch

## API Requirements
All solutions require:
- OpenAI API key (or alternatives: Hugging Face, OpenRouter, Together AI, etc.)
- SerperDev API key for web search functionality

## Frontend Guidelines
- Use existing CSS classes for consistency
- Maintain responsive design for mobile compatibility
- Code blocks use Prism.js for syntax highlighting
- Google Analytics implemented with GDPR-compliant cookie consent

## Important Notes
- Each solution demonstrates specific CrewAI patterns and should remain educational
- Verbose mode is enabled on agents for learning purposes
- Solutions link to external GitHub repository for additional examples
- Website is automatically published via GitHub Pages from main branch