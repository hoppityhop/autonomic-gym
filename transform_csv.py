import pandas as pd
import json
from models.exercise import Exercise
from CRUD.exercise_repo import create_exercise, add_secondary_muscle, add_primary_muscle_to_exercise

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
        
        new_exercise = Exercise(
            force=data[i]['force'].upper(),
            name=data[i]['name'],
            instructions=instructions,
            level=data[i]['level'].upper(),
            mechanic=data[i]['mechanic'],
            avg_time_per_set=43
        )
        
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