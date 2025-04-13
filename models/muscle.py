from sqlalchemy import *
from sqlalchemy.orm import Mapped, relationship
# from exercise import Exercise

from .base import BaseModel


class Muscle(BaseModel):
    __tablename__ = "muscle"

    # Name should be the primary key for this table
    name = Column(String(50), primary_key=True, nullable=False, unique=True)

    # exercises: Mapped[list["Exercise"]] = relationship("Exercise", back_populates="muscle")
    exercises = relationship("Exercise", back_populates="primary_muscle")
