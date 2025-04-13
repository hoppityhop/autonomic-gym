from sqlalchemy import Column, Integer

from models.setup import Base


class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    # id = Column(Integer, primary_key=True)
