from sqlalchemy.orm import Session, joinedload
from db import SessionLocal
from models.workout_session import WorkoutSession


def create_step(workout_step_to_create, related_workout_session_id):
    """
    Create a new workout step in the database.
    This function checks whether a workout step with the same primary key already exists.
    Then it creates a new workout step, adds it to the session, and commits the session.
    :param workout_step_to_create:
    :param related_workout_session_id:
    :return:
    """
