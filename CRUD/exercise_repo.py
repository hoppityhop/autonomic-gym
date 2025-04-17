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
        ex_name = exercise_to_create.name
        existing_exercise = session.query(Exercise).filter_by(name=ex_name).first()

        if existing_exercise:
            print(f"Exercise '{exercise_to_create.name}' already exists in the database.")
            return ex_name

        # Create a new Exercise object
        session.add(exercise_to_create)
        session.commit()
    return ex_name


def add_primary_muscle_to_exercise(prim_muscle: Muscle, exercise_name):
    """
    Add a primary muscle to an exercise.
    This function checks if the primary muscle already exists in the database.
    If it does, it adds the primary muscle to the exercise and commits the session.

    Args:
        prim_muscle (_type_): _description_
        exercise (_type_): _description_
    """
    with SessionLocal() as session:
        # Check whether a primary muscle already exists on the exercise
        exercise = session.query(Exercise).filter_by(name=exercise_name).first()
        if exercise.primary_muscle:
            print(f"Exercise '{exercise.name}' already has a primary muscle.")
            return exercise
        else:
            # Add the primary muscle to the exercise
            #Get primary muscle from database
            prim_muscle = session.query(Muscle).filter_by(name=prim_muscle).first()
            exercise.primary_muscle = prim_muscle
            session.commit()
            return exercise
