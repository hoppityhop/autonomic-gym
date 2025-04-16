from sqlalchemy import *
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from models.muscle import Muscle
import enum


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
    primary_muscle: Mapped[Muscle] = relationship(back_populates="exercises")

    # secondary muscles (list)
