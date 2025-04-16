from db.session import SessionLocal, engine
from models import Base
from models.exercise import Exercise
from models.muscle import Muscle


Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)