from sqlalchemy.orm import Session
from db import SessionLocal
from models.workout_session import WorkoutSession
from models.workout_step import WorkoutStep


def create_workout_session(workout_session_to_create):
    """
    Create a new workout session in the database.
    This function checks whether a workout session with the same uuid already exists.
    If it does, it returns the existing workout session.
    If it doesn't, it creates a new workout session, adds it to the session, and commits the session.
    :param workout_session_to_create: contains id, entry_time,
    :return:
    """

    with SessionLocal() as session:
        # Check whether a workout session with the same uuid already exists
        existing_workout_session = session.query(WorkoutSession).filter_by(id=workout_session_to_create["id"]).first()
        if existing_workout_session:
            print(f"Workout session '{existing_workout_session.id}' already exists in the database.")
            return existing_workout_session
        # Create a new WorkoutSession object
        new_workout_session = WorkoutSession(id=workout_session_to_create['id'],
            entry_time=workout_session_to_create["entry_time"], cum_wait_time=0, status="IDLE")
        # Add the new workout session to the session
        session.add(new_workout_session)
        session.commit()
        session.refresh(new_workout_session)
        return new_workout_session
