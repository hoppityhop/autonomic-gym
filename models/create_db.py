from setup import engine, Base
from exercise import Exercise
from muscle import Muscle

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)