from crewai import Task

from agents import (
    game_designer,
    senior_engineer,
    qa_engineer
)

def create_tasks(game_idea):
    """
    Creates all CrewAI tasks.
    """

    # Task 1 - Game Design
    
    designer_task = Task(
        description=f"""
The user wants the following game:

{game_idea}

Create a complete Game Design Document.

Include:

1. Game Title
2. Genre
3. Objective
4. Controls
5. Player
6. Enemies
7. Obstacles
8. Powerups (if any)
9. Scoring System
10. Core Mechanics
11. Win Condition
12. Lose Condition

Keep the game simple enough to be implemented in ONE
Python file using Pygame.
""",

        expected_output="""
A complete markdown Game Design Document.
""",

        agent=game_designer
    )

    # Task 2 - Develop Game
    
    developer_task = Task(
        description="""
Use ONLY the Game Design Document provided by the previous task.

Generate a complete working Pygame application.

Requirements:

- Import pygame
- Import sys
- Import random (if required)

The game must contain:

- Initialization
- Main game loop
- Event handling
- Rendering
- Collision detection
- Score system
- Restart support
- Quit support

IMPORTANT:

Return ONLY executable Python code.

Wrap everything inside:

```python
# code
```
""",
expected_output="""

A complete runnable Python game wrapped inside a markdown
python code block.
""",

    context=[designer_task],

    agent=senior_engineer
)


# Task 3 - QA Review

    review_task = Task(
        description="""

    Review the Python code produced in the previous task.

    Do NOT redesign the game.

    Do NOT change the gameplay unless required to fix a bug.

    Check:

    Syntax
    Missing imports
    Runtime issues
    Game loop
    Collision detection
    Readability
    Best practices

    If the code is already correct,
    return the SAME code.

    Your response MUST follow this format exactly:

    Game Review

    Short review.

    Python Code
    # complete corrected code
    Requirements

    pip install pygame
    """,

        expected_output="""

    A review followed by the complete Python code inside a
    python block.
    """,

        context=[developer_task],

        agent=qa_engineer
    )

    return (
        designer_task,
        developer_task,
        review_task
    )