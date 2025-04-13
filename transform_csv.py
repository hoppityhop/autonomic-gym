from models.setup import engine, Session
from models.exercise import Exercise
from models.muscle import Muscle
import pandas as pd
import json

# Load the CSV file
csv_file_path = 'exercisedb.csv'
df = pd.read_csv(csv_file_path)
# Convert the DataFrame to a list of dictionaries
data = df.to_dict(orient='records')

local_session = Session(bind=engine)
# List of objects to add_all with in the session after the for loop
all_exercises = []

for i in range(1, len(data)):
    print(data[i])
    new_exercise = Exercise(force=data[i]['force'].upper(), name=data[i]['name'], description=data[i]['instructions'],
                            level=data[i]['level'].upper(), mechanic=data[i]['mechanic'], avg_time_per_set=43)
    # Add the primary muscle
    primary_muscle_name = data[i]['primaryMuscles']

    #Remove all punctuation from the primary muscle name
    primary_muscle_name = ''.join(char for char in primary_muscle_name if char.isalnum() or char.isspace())

    # Query DB to retrieve the primary muscle using SQLAlchemy ORM
    primary_muscle = local_session.query(Muscle).filter_by(name=primary_muscle_name).first()

    if primary_muscle:
        new_exercise.primary_muscle = primary_muscle
    else:
        print(f"Primary muscle '{primary_muscle_name}' not found in the database.")
        continue

    all_exercises.append(new_exercise)
    #Write to the database
    # local_session.add(new_exercise)
local_session.add_all(all_exercises)
local_session.commit()
