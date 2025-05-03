from sqlalchemy import ForeignKey, Integer, Table, Column
from models import Base

# Association table for secondary muscles
secondary_muscles_association = Table(
    'exercise_secondary_muscles', Base.metadata,
    Column('association_id', Integer, primary_key=True),
    Column('exercise_id', ForeignKey('exercise.id')),
    Column('muscle_name', ForeignKey('muscle.name'))
)

equipment_exercise_association = Table(
    'equipment_exercise', Base.metadata,
    Column('association_id', Integer, primary_key=True),
    Column('equipment_id', ForeignKey('equipment.id')),
    Column('exercise_id', ForeignKey('exercise.id'))
)
