import pandas as pd
import json
from models.exercise import Exercise
from CRUD.exercise_repo import create_exercise, add_primary_muscle_to_exercise

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
        created_exercise = create_exercise(new_exercise)

        primary_muscle_to_add = data[i]['primaryMuscles'][2:-2]
        add_primary_muscle_to_exercise(primary_muscle_to_add, created_exercise.name)

        
        # with Session(bind=engine) as session:
        #     try:
        #         new_exercise = Exercise(
        #             force=data[i]['force'].upper(),
        #             name=data[i]['name'],
        #             description=data[i]['instructions'],
        #             level=data[i]['level'].upper(),
        #             mechanic=data[i]['mechanic'],
        #             avg_time_per_set=43
        #         )

        #         # Clean and query the primary muscle
        #         primary_muscle_name = ''.join(char for char in data[i]['primaryMuscles'] if char.isalnum() or char.isspace())
        #         primary_muscle = session.query(Muscle).filter_by(name=primary_muscle_name).first()

        #         if primary_muscle:
        #             new_exercise.primary_muscle = primary_muscle
        #             session.add(new_exercise)
        #             session.commit()
        #         else:
        #             print(f"Primary muscle '{primary_muscle_name}' not found in the database.")
        #     except Exception as e:
        #         print(f"Error processing record {i}: {e}")
        #         session.rollback()
