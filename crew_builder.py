from crewai import Crew, Process

from agents import (
    game_designer,
    senior_engineer,
    qa_engineer
)

from tasks import create_tasks

def create_crew(game_idea):
    """
    Creates and returns the CrewAI workflow.
    """

    # Create Tasks
    designer_task, developer_task, review_task = create_tasks(game_idea)

    # Create Crew
    crew = Crew(
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

        verbose=True,

        memory=False
    )

    return crew