from CRUD import muscle_repo
from db import SessionLocal
from models.exercise import Exercise
from transform_csv import transform_csv_file
from CRUD.exercise_repo import create_exercise
from create_db import create_the_db

create_the_db()

# The code below is used to populate the Muscle table with the muscle names
all_muscles = ['abdominals', 'abductors', 'adductors', 'middle back', 'biceps', 'calves', 'chest', 'forearms', 'glutes',
               'hamstrings', 'lats', 'lower back', 'neck', 'quadriceps', 'shoulders', 'traps', 'triceps']

for m in all_muscles:
    new_muscle = muscle_repo.create_muscle(m)

# Try to transform and print exercises
transform_csv_file()

# Quick test to see if the exercises are being created
test_exercise = "Atlas Stones"

with SessionLocal() as session:
    exercise = session.query(Exercise).filter(Exercise.name == test_exercise).first()
    if exercise:
        print(f"Exercise found: {exercise.name}")
        print(exercise)
    else:
        print(f"Exercise '{test_exercise}' not found.")
