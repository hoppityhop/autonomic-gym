from CRUD import muscle_repo
from models.exercise import Exercise
from transform_csv import transform_csv_file
from CRUD.exercise_repo import create_exercise


# The code below is used to populate the Muscle table with the muscle names
all_muscles = ['abdominals', 'abductors', 'adductors', 'middle back', 'biceps', 'calves', 'chest', 'forearms', 'glutes',
               'hamstrings', 'lats', 'lower back', 'neck', 'quadriceps', 'shoulders', 'traps', 'triceps']

for m in all_muscles:
    new_muscle = muscle_repo.create_muscle(m)
    

# Try to transform and print exercises
transform_csv_file()

