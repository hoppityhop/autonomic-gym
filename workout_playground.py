from CRUD import muscle_repo
from db import SessionLocal
from models.exercise import Exercise
from transform_csv import transform_csv_file, transform_equipment_csv
from CRUD.exercise_repo import create_exercise
from create_db import create_the_db
from CRUD.workout_session_repo import create_workout_session


sample_dict = {"uuid": "session-015", "entry_time": 2, "steps": [
    {"sequence_number": 1, "equipment_name": "machine_leg_extension_1", "priority_score": 25, "est_time": 6,
        "num_sets": 4},
    {"sequence_number": 2, "equipment_name": "linear_leg_press_2", "priority_score": 34, "est_time": 11, "num_sets": 3},
    {"sequence_number": 3, "equipment_name": "machine_shoulder_press", "priority_score": 18, "est_time": 7,
        "num_sets": 4},
    {"sequence_number": 4, "equipment_name": "glute_kickback", "priority_score": 22, "est_time": 10, "num_sets": 4},
    {"sequence_number": 5, "equipment_name": "machine_leg_curl_2", "priority_score": 12, "est_time": 9, "num_sets": 4}]}

sesh_model = {
    "id": sample_dict["uuid"],
    "entry_time": sample_dict["entry_time"],
}

create_workout_session(sesh_model)