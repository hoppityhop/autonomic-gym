from typing import List

from sqlalchemy import *
from sqlalchemy.orm import Mapped, mapped_column

from models import Base
from models.exercise import Exercise
import enum


class Status(enum.Enum):
    MAINTENANCE = 'maintenance'
    AVAILABLE = 'available'
    IN_USE = 'in_use'


class Equipment(Base):
    __tablename__ = 'equipment'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)

    # Estimated completion time in integer value (representing minutes since 6 PM)
    estimated_completion_time: Mapped[int] = mapped_column(Integer, nullable=True)

    # Status of the equipment
    status: Mapped[Status] = mapped_column(Enum(Status), nullable=False)

    # TODO: Equipment has a one to one relationship with the current user. This can also be null
    # if the equipment is not in use

    # TODO: Equipment has a many to many relationship with exercises

    # TODO: potential extensions include maintenance mode, enumerated exercise category, and possibly a queue of   #  user sessions
