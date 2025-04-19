from db.session import SessionLocal, engine
from models import Base
from models.exercise import Exercise
from models.muscle import Muscle


def create_the_db():
    """
    Create the database and tables.
    This function creates the database and tables if they do not exist.
    It also drops all existing tables and creates new ones.
    """
    Base.metadata.drop_all(engine)

    Base.metadata.create_all(engine)