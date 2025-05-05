from typing import Set, List
from sqlalchemy import *
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.equipment import Equipment
from models.muscle import Muscle
import enum
from models.associations import secondary_muscles_association


class Force(enum.Enum):
    PUSH = 'push'
    PULL = 'pull'


class Level(enum.Enum):
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    EXPERT = 'expert'


class Mechanic(enum.Enum):
    COMPOUND = 'compound'
    ISOLATION = 'isolation'


class Exercise(Base):
    __tablename__ = 'exercise'

    id: Mapped[int] = mapped_column(primary_key=True)
    force: Mapped[Force] = mapped_column(Enum(Force), nullable=False)

    name: Mapped[str] = mapped_column(String(256), nullable=False)
    level: Mapped[Level] = mapped_column(Enum(Level), nullable=False)

    instructions: Mapped[str] = mapped_column(Text())
    mechanic: Mapped[Mechanic] = mapped_column(Enum(Mechanic), nullable=True)

    # in seconds
    avg_time_per_set: Mapped[int] = mapped_column(Integer, nullable=False)

    # primary muscle
    primary_muscle_name: Mapped[str] = mapped_column(ForeignKey("muscle.name"), nullable=True)
    primary_muscle: Mapped[Muscle] = relationship(back_populates="primary_exercises")

    # secondary muscles (list)
    secondary_muscles: Mapped[Set[Muscle]] = relationship("Muscle", secondary="exercise_secondary_muscles",
                                                          back_populates="secondary_exercises")

    related_equipment: Mapped[Set[Equipment]] = relationship("Equipment", secondary="equipment_exercise",
                                                             back_populates="related_exercises")

    workout_steps: Mapped[List["WorkoutStep"]] = relationship(back_populates="exercise")

    # String representation of the exercise
    def __repr__(self):
        return f"<Exercise(name={self.name}, force={self.force}, level={self.level}, mechanic={self.mechanic}, primary_muscle={self.primary_muscle_name}, secondary_muscles={self.secondary_muscles})>"
