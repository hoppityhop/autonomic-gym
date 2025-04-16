from sqlalchemy.orm import Session
from db import SessionLocal
from models.exercise import Exercise
from models.muscle import Muscle


def test_create_exercise(exercise_to_create: Exercise):
    """Test the create_exercise function."""
    # Create a new exercise
    new_exercise = exercise_to_create
    assert new_exercise.name == "Bench Press"
    assert new_exercise.force == "Push"
    assert new_exercise.level == "Intermediate"
    assert new_exercise.instructions == "Lie on a bench and press the barbell up and down."
    assert new_exercise.mechanic == "Compound"
    assert new_exercise.avg_time_per_set == 60
    
    with SessionLocal() as session:
        # Check if the exercise exists in the database
        existing_exercise = session.query(Exercise).filter_by(name="Bench Press").first()
        
        if existing_exercise:
            print(f"Exercise '{existing_exercise.name}' exists in the database.")
            return existing_exercise
        else:
            # Create and add the new exercise to the session
            session.add(new_exercise)
            session.commit()
            return new_exercise
            

def create_exercise(exercise_to_create: Exercise):
    """
    Create a new exercise in the database.
    This function checks if an exercise with the same name 
    already exists in the database. Then it creates a new exercise, adds
    it to the session, and commits the session.

    Args:
        force (_type_): _description_
        name (_type_): _description_
        level (_type_): _description_
        instructions (_type_): _description_
        mechanic (_type_): _description_
        avg_time_per_set (_type_): _description_
    """
    with SessionLocal() as session:
        # Check whether an exercise with the same name already exists
        existing_exercise = session.query(Exercise).filter_by(name=exercise_to_create.name).first()

        if existing_exercise:
            print(f"Exercise '{exercise_to_create.name}' already exists in the database.")
            return existing_exercise

        # Create a new Exercise object
        session.add(exercise_to_create)
        session.commit()
        return exercise_to_create
