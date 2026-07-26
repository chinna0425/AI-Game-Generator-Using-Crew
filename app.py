import os
from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool


# Load Environment Variables


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

if not serper_api_key:
    raise ValueError("SERPER_API_KEY not found in .env file")


# Initialize LLM


llm = LLM(
    model="gemini/gemini-3.5-flash",
    api_key=gemini_api_key
)


# Initialize Search Tool


search_tool = SerperDevTool(
    api_key=serper_api_key
)


# Agent 1 : Game Designer


game_designer = Agent(
    role="Creative Game Designer",

    goal=(
        "Create fun, engaging and feasible 2D game ideas "
        "that can be implemented using Python and Pygame."
    ),

    backstory="""
You are an experienced Game Designer with years of experience
designing arcade games.

You convert simple ideas into complete game design documents.

Your design should include:

- Game title
- Genre
- Objective
- Controls
- Player
- Enemies
- Obstacles
- Items
- Win condition
- Lose condition
- Core mechanics

Keep the scope small enough to build using a single Python
file with Pygame.
""",

    llm=llm,

    verbose=True
)


# Agent 2 : Senior Python Developer


senior_engineer = Agent(
    role="Senior Python Game Developer",

    goal=(
        "Develop complete and runnable Pygame games "
        "based on the provided Game Design Document."
    ),

    backstory="""
You are a senior Python developer specializing in Pygame.

You always generate:

- Clean Python code
- Proper comments
- Organized structure
- Event handling
- Collision detection
- Drawing logic
- Game loop
- Score system
- Restart/Quit support

The code should be directly executable.
""",

    llm=llm,

    tools=[search_tool],

    verbose=True
)


# Agent 3 : QA Engineer


qa_engineer = Agent(
    role="QA Engineer & Code Reviewer",

    goal=(
        "Review generated game code and improve its "
        "quality, readability and correctness."
    ),

    backstory="""
You are a meticulous QA Engineer.

You verify:

- Syntax errors
- Runtime issues
- Missing features
- Game balance
- Code quality
- Comments
- Readability
- Best practices

Always provide the final improved version of the code.
""",

    llm=llm,

    verbose=True
)


# Get User Input


game_idea = input("\nEnter your game idea: ").strip()


# Task 1 : Game Design


designer_task = Task(
    description="""
Take the user's game idea:

{game_idea}

Create a simple and fun 2D game that can be developed using
Python and Pygame.

Your Game Design Document should include:

1. Game Title
2. Genre
3. Objective
4. Controls
5. Player
6. Enemies
7. Obstacles
8. Items
9. Game Mechanics
10. Win Condition
11. Lose Condition

Keep the project small enough to be implemented in a
single Python file.
""",

    expected_output="""
A complete markdown Game Design Document containing
all gameplay details.
""",

    agent=game_designer
)


# Task 2 : Game Development


developer_task = Task(
    description="""
Using the Game Design Document from the previous task,
develop a COMPLETE Python game using Pygame.

Requirements:

- Import pygame
- Import sys
- Import random if needed

Include:

- Game initialization
- Event handling
- Game loop
- Player movement
- Collision detection
- Obstacles
- Score
- Rendering
- Quit handling

The generated code should be executable directly using

python game.py

Return ONLY the Python source code followed by a short
section explaining how to play the game.
""",

    expected_output="""
A complete runnable Python game written using Pygame.
""",

    context=[designer_task],

    agent=senior_engineer
)


# Task 3 : QA Review


review_task = Task(
    description="""
Review the generated Python game.

Verify:

- Syntax errors
- Runtime issues
- Missing imports
- Missing game loop
- Bugs
- Gameplay
- Code quality
- Readability
- Comments

If improvements are required,
modify the code.

Return the FINAL improved version.

Do not omit any part of the code.
""",

    expected_output="""
The final answer should contain:

1. Complete Python source code

2. Instructions explaining how to play the game.
""",

    context=[designer_task, developer_task],

    agent=qa_engineer
)


# Crew Configuration


game_crew = Crew(

    agents=[
        game_designer,
        senior_engineer,
        qa_engineer
    ],

    tasks=[
        designer_task,
        developer_task,
        review_task
    ],

    process=Process.sequential,

    verbose=True
)



# Execute Crew


def main():
    print("\n" + "=" * 60)
    print("🎮 AI Game Generator using CrewAI")
    print("=" * 60)

    try:
        print("\n🚀 Generating your game...\n")

        result = game_crew.kickoff(
            inputs={
                "game_idea": game_idea
            }
        )

        print("\n" + "=" * 60)
        print("✅ GAME GENERATED SUCCESSFULLY")
        print("=" * 60)

        print(result)

        # Convert CrewOutput to string
        final_output = str(result)

        # Save complete output
        with open("generated_game.txt", "w", encoding="utf-8") as file:
            file.write(final_output)

        # Try to extract Python code
        if "```python" in final_output:
            start = final_output.find("```python") + len("```python")
            end = final_output.find("```", start)

            python_code = final_output[start:end].strip()

            with open("generated_game.py", "w", encoding="utf-8") as file:
                file.write(python_code)

            print("\n Python game saved as:")
            print("generated_game.py")

        print("\n Full response saved as:")
        print("generated_game.txt")

    except Exception as e:
        print("\nError while generating the game")
        print(e)



# Run Application


if __name__ == "__main__":
    main()