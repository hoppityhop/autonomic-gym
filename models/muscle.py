from typing import List

from sqlalchemy import *
from sqlalchemy.orm import Mapped, relationship, mapped_column
from models import Base


class Muscle(Base):
    __tablename__ = 'muscle'

    name: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False, unique=True)

    primary_exercises: Mapped[List["Exercise"]] = relationship(back_populates="primary_muscle")

    secondary_exercises: Mapped[List["Exercise"]] = relationship(
        "Exercise",
        secondary="exercise_secondary_muscles",
        back_populates="secondary_muscles"
    )

    def __repr__(self):
        return f"<Muscle(name={self.name})>"
