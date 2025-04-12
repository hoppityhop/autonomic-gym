from sqlalchemy import (Column, ForeignKey, Integer, String, DateTime, Boolean, create_engine)
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship, sessionmaker

# from models.exercise import Exercise
# from models.muscle import Muscle


DATABASE_URL = "sqlite:///gymdb.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker()

