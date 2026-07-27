from crew_builder import create_crew
from output_parser import parse_output

def generate_game(game_idea):
    """
    Generates a complete game using CrewAI.
    """

    if not game_idea.strip():
        raise ValueError("Game idea cannot be empty.")

    try:
        
        # Create Crew
        
        crew = create_crew(game_idea)

        # Execute Crew
        
        result = crew.kickoff()

        print("\n" + "=" * 80)
        print("CREW EXECUTION COMPLETED")
        print("=" * 80)

        print("\nResult Type:")
        print(type(result))

        print("\nResult:")
        print(result)

        # Debug Task Outputs (Latest CrewAI)  

        if hasattr(result, "tasks_output"):

            print("\nTask Outputs")
            print("=" * 80)

            for index, task in enumerate(result.tasks_output, start=1):

                print(f"\nTask {index}")
                print("-" * 40)

                if hasattr(task, "raw"):
                    print(task.raw)
                else:
                    print(task)

        # Parse Final Output        

        parsed = parse_output(result)

        return parsed

    except Exception as e:

        print("\n" + "=" * 80)
        print("ERROR DURING GAME GENERATION")
        print("=" * 80)
        print(e)

        raise e