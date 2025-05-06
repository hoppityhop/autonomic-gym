from CRUD.workout_session_repo import get_session_by_entry_time

def check_new_sessions(minute):
    """
    Checks if there are new sessions beginning at the given minute.
    :param minute:
    :return:
    """
    # This function queries the database for new sessions beginning at the given minute.
    new_sessions = get_session_by_entry_time(minute)
    return new_sessions