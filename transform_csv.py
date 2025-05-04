import pandas as pd
import json

from models.equipment import Equipment
from models.exercise import Exercise
from CRUD.exercise_repo import create_exercise, add_secondary_muscle, add_primary_muscle_to_exercise
from CRUD.equipment_repo import create_equipment, add_exercise_to_equipment, get_equipment_by_name

def transform_csv_file():
    # Load the CSV file
    csv_file_path = 'exercisedb.csv'
    df = pd.read_csv(csv_file_path)
    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict(orient='records')

    # List of objects to add_all with in the session after the for loop
    all_exercises = []

    for i in range(1, len(data)):
        print(data[i])

        instructions = data[i]['instructions'][2:-2]

        new_exercise = Exercise(force=data[i]['force'].upper(), name=data[i]['name'], instructions=instructions,
                                level=data[i]['level'].upper(), mechanic=data[i]['mechanic'], avg_time_per_set=43)

        # Call the create_exercise method to add the new exercise to the session
        ex_name = create_exercise(new_exercise)

        primary_muscle_to_add = data[i]['primaryMuscles'][2:-2]
        add_primary_muscle_to_exercise(primary_muscle_to_add, ex_name)

        secondary_muscles = data[i]['secondaryMuscles'][2:-2].split(',')
        for sec_muscle in secondary_muscles:
            # Clean string of all punctuation and whitespace
            sec_muscle = sec_muscle.strip().replace("'", "").replace('"', "").replace('[', '').replace(']', '')
            add_secondary_muscle(sec_muscle, ex_name)
        print(data[i]['secondaryMuscles'])


def transform_equipment_csv():
    # Load the CSV file
    csv_file_path = 'equipment.csv'
    df = pd.read_csv(csv_file_path)
    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict(orient='records')

    all_equipment = []

    for i in range(len(data)):
        print(data[i])

        # Clean string of all punctuation and whitespace
        equipment_name = data[i]['machine_name'].strip().replace("'", "").replace('"', "").replace('[', '').replace(']', '')
        # Create a new Equipment object
        new_equipment = Equipment(id=data[i]['id'], name=equipment_name, estimated_completion_time=None,
                                  status="AVAILABLE")

        print("Stop here")

        result = create_equipment(new_equipment)
        print(result + " was returned successfully.")

        related_exercises = data[i]['workouts'][2:-2].split(',')
        # print(related_exercises)

        for rel in related_exercises:
            # Clean string of all punctuation and whitespace
            rel = rel.strip().replace("'", "").replace('"', "").replace('[', '').replace(']', '')
            print(rel)
            add_exercise_to_equipment(rel, result)

        # Check for equipment in DB
        equipment = get_equipment_by_name(equipment_name)
        str_equipment = str(equipment)
        print(equipment)
