from setup import engine, Session
from models.exercise import Exercise
from models.muscle import Muscle

local_session = Session(bind=engine)

all_muscles = ['abdominals', 'abductors', 'adductors', 'back', 'biceps', 'calves', 'chest', 'forearms', 'glutes',
               'hamstrings', 'lats', 'lower', 'middle', 'neck', 'quadriceps', 'shoulders', 'traps', 'triceps']
example_exercise = Exercise(name="Squat", description="A compound exercise that targets the legs and glutes.",
                            level="INTERMEDIATE", mechanic="ISOLATION", avg_time_per_set=60)

# Add example exercise to the session
local_session.add(example_exercise)
# Write to the database
local_session.commit()

example_muscle = Muscle(name="legs")
# Add the example exercise to the muscle
example_muscle.exercises.append(example_exercise)
# Add the example muscle to the session
local_session.add(example_muscle)
# Write to the database
local_session.commit()  # for m in muscles:

