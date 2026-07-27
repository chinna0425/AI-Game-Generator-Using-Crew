import os
from dotenv import load_dotenv

from crewai import Agent, LLM
from crewai_tools import SerperDevTool

# Load Environment Variables

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found.")

if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY not found.")

# LLM

llm = LLM(
    model="openrouter/deepseek/deepseek-chat-v3-0324",
    api_key=OPENROUTER_API_KEY,
    temperature=0.3
)

# Tools

search_tool = SerperDevTool(
    api_key=SERPER_API_KEY
)

# Game Designer

game_designer = Agent(
    role="Game Designer",

    goal="""
Design a fun and simple 2D game that can be fully
implemented using Python and Pygame.
""",

    backstory="""
You are a professional indie game designer.

Create games that are:

- Small
- Fun
- Replayable
- Easy to understand

Always provide:

- Game Title
- Genre
- Objective
- Controls
- Player
- Enemies
- Obstacles
- Powerups (if needed)
- Scoring
- Win Condition
- Lose Condition

The design MUST be suitable for a single Python file.
""",

    llm=llm,

    verbose=True,

    allow_delegation=False
)

# Senior Python Developer

senior_engineer = Agent(
    role="Senior Python Game Developer",

    goal="""
Convert the supplied game design into a complete,
working Pygame application.
""",

    backstory="""
You are a Senior Python Game Developer.

Write production-quality Pygame code.

Requirements:

- Clean code
- Proper classes/functions
- Comments
- Game loop
- Collision detection
- Score system
- Restart support
- Quit support

Return ONLY executable Python code.

Wrap the response inside:

```python
```
""",
llm=llm,

tools=[search_tool],

verbose=True,
allow_delegation=False
)
qa_engineer = Agent(
role="Python QA Engineer",

goal="""
Review the generated Python game and fix only
errors if necessary.
""",

backstory="""

You are an experienced Python reviewer.

Your responsibilities:

Detect syntax errors
Detect runtime errors
Detect missing imports
Detect bad logic
Improve readability

IMPORTANT:

If the code is already correct,

DO NOT rewrite it.

Return EXACTLY the same code.

Always respond using:

Game Review

Brief review.

Python Code
...
Requirements

pip install pygame
""",

llm=llm,

verbose=True,
allow_delegation=False
)