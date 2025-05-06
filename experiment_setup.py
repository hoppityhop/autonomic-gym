import json
from models.equipment import Equipment
from models.exercise import Exercise
from CRUD.exercise_repo import create_exercise, add_secondary_muscle, add_primary_muscle_to_exercise
from CRUD.equipment_repo import create_equipment, add_exercise_to_equipment, get_equipment_by_name


# Load the JSON file "parsed_data.json"
with open('parsed_data.json', 'r') as file:
    data = json.load(file)
print("pause")