from sqlalchemy import (Column, ForeignKey, Integer, String, DateTime, Boolean, create_engine)
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship, sessionmaker

# from models.exercise import Exercise
# from models.muscle import Muscle


Base = declarative_base()
DATABASE_URL = "sqlite:///gymdb.db"
engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)


def create_tables():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


# class BaseModel(Base):
#     __abstract__ = True
#     __allow_unmapped__ = True
#
#     id = Column(Integer, primary_key=True)


from models.exercise import Exercise
from models.muscle import Muscle

Base.metadata.create_all(engine)


# Main method
#
# if __name__ == "__main__":
#     # Create tables
#     create_tables()
