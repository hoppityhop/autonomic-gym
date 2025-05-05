from CRUD.workout_session_repo import create_workout_session
from CRUD.step_repo import create_step


def create_session_with_steps(session_metadata, steps_list):
    """
    Creates a workout session and adds all its steps using the CRUD functionalities in workout session repo and steps repo.
    :param session_metadata: dictionary with id and entry_time
    :param steps_list: list of the steps to be performed
    :return:
    """

    # Create the workout session
    workout_session = create_workout_session(session_metadata)
    prev_time = session_metadata["entry_time"]

    # Iterate through the steps and create each one from the list
    for step in steps_list:
        # Create a new workout step
        step_res = create_step(step, workout_session.id, prev_time)
        prev_time = step_res.est_end_time
        print(step)

