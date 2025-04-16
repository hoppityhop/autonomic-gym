from sqlalchemy import *
from sqlalchemy.orm import Mapped, relationship, mapped_column
from models import Base


class Muscle(Base):
    __tablename__ = 'muscle'

    name: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False, unique=True)

