from sqlalchemy.orm import Session, joinedload
from db import SessionLocal
from models.equipment import Equipment
from models.workout_session import WorkoutSession
from models.workout_step import WorkoutStep


def create_step(workout_step_to_create, related_workout_session_id, prev_end_time):
    """
    Create a new workout step in the database.
    This function checks whether a workout step with the same primary key already exists.
    Then it creates a new workout step, adds it to the session, and commits the session.
    :param workout_step_to_create:
    :param related_workout_session_id:
    :return:
    """

    with SessionLocal() as session:
        # Check whether a workout step with the same equipment id and session id already exists
        existing_workout_step = session.query(WorkoutStep).filter_by(
            equipment_id=workout_step_to_create["equipment_name"],
            workout_session_id=related_workout_session_id,
            # sequence_number=workout_step_to_create["sequence_number"]
        ).first()
        if existing_workout_step:
            print(f"Workout step '{existing_workout_step.id}' already exists in the database.")
            return existing_workout_step

        # Get the related workout session using its id
        related_workout_session = session.query(WorkoutSession).filter_by(id=related_workout_session_id).first()
        related_equipment = session.query(Equipment).filter_by(id=workout_step_to_create["equipment_name"]).first()
        selected_exercise_from_equipment = related_equipment.related_exercises[0]
        # Create a new WorkoutStep object
        new_workout_step = WorkoutStep(
            sequence_number=workout_step_to_create["sequence_number"],
            # equipment_id=workout_step_to_create["equipment_name"],
            priority_score=workout_step_to_create["priority_score"],
            estimated_time=workout_step_to_create["est_time"],
            sets=workout_step_to_create["num_sets"],
            est_start_time=prev_end_time + 1,
            est_end_time=prev_end_time + 1 +  workout_step_to_create["est_time"] )
        # Add workout session to the step
        new_workout_step.workout_session = related_workout_session
        new_workout_step.equipment = related_equipment
        new_workout_step.exercise = selected_exercise_from_equipment
        # Add the new workout step to the session
        session.add(new_workout_step)
        # Commit the session to save the new workout step to the database
        session.commit()
        session.refresh(new_workout_step)
        return new_workout_step
