# This file contains the logic driving the simulation. It initializes the simulation, creates a workout session,
# and simulates the workout process for all sessions active.
# It iterates minute-by-minute from 0 to 300.
# At each minute, it:
# 1. Checks whether a new person has entered the gym.
# 2. Checks whether a workout step has ended and the state of the machine.
# 3. Checks whether a workout step has started.
from simulation_logic.helpers import check_new_sessions

active_session_ids = []

for minute in range(1, 101):
    # Check if any new sessions have begun at this time (uses the database)
    new_sessions = check_new_sessions(minute)
    if not new_sessions:
        print("No new sessions at minute " + str(minute))
    else:
        print(str(new_sessions) + " at minute " + str(minute))
    # Push the new sessions' ids to the active_session_ids list
        for session in new_sessions:
            active_session_ids.append(session.id)
            print("New session added: " + str(session.id))

    # TODO: call an activate session function in the session_management directory
pass
    # TODO: Check if any sessions are complete
    # TODO: Check whether a step is complete
    # TODO: If session is idle, check for the availability of the equipment in the next step



