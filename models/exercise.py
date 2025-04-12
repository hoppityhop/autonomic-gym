from sqlalchemy import *
from sqlalchemy.orm import relationship, Mapped
# from muscle import Muscle

from base import BaseModel


class Exercise(BaseModel):
    __tablename__ = "exercise"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(50), nullable=False)
    # Equipment will need to be related to an Equipment row through a foreign key

    # Level should be ENUM (BEGINNER, INTERMEDIATE, ADVANCED)
    level = Column(Enum("BEGINNER", "INTERMEDIATE", "ADVANCED"), nullable=False)
    # Description
    description = Column(String(500), nullable=False)
    mechanic = Column(Enum("COMPOUND", "ISOLATION"), nullable=True)

    # primary_muscle with the name of the muscle as the foreign key
    primary_muscle_name = Column(String(50), ForeignKey("muscle.name"), nullable=True)
    primary_muscle = relationship("Muscle", back_populates="exercises")
    # Secondary muscles as a list

    avg_time_per_set = Column(Integer, nullable=False)  # in seconds
