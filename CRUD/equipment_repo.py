from sqlalchemy.orm import Session
from db import SessionLocal
from models.exercise import Exercise
from models.muscle import Muscle
from models.equipment import Equipment


def test_create_equipment(equipment_to_create: Equipment):
    """Test of creating equipment"""


def create_equipment(equipment_to_create: Equipment):
    """
    Create a new piece of equipment in the database. This function checks whether a piece of equipment with the same primary key already exsits. Then it creates a new piece of equipment, adds it to the session, and commits the session.
    :param equipment_to_create: Equipment object to be created
    :return:
    """
    with SessionLocal() as session:
        # Check whether a piece of equipment with the same primary key already exists
        eq_id = equipment_to_create.id
        existing_equipment = session.query(Equipment).filter_by(id=eq_id).first()

        if existing_equipment:
            print(f"Equipment '{equipment_to_create.name}' already exists in the database.")
            return eq_id

        # Create a new piece of Equipment
        session.add(equipment_to_create)
        session.commit()
        # print(f"Equipment '{equipment_to_create.id}' created successfully.")
        return equipment_to_create.id
    return "Success"


def add_exercise_to_equipment(related_ex_name, related_eq_id):
    """
    Add an exercise to a piece of equipment in the database.
    This function checks whether the equipment and exercise exist in the database.
     Then it creates a new relationship
    between the two, adds it to the session, and commits the session.
    :param related_ex:
    :param related_eq:
    :return:
    """

    with SessionLocal() as session:
        # Check whether the same exercise exists for that piece of equipment
        existing_exercise = session.query(Exercise).filter_by(name=related_ex_name).first()
        existing_equipment = session.query(Equipment).filter_by(id=related_eq_id).first()

        if not existing_exercise:
            print(f"Exercise '{related_ex_name}' does not exist in the database.")
            return "Exercise not found"

        if not existing_equipment:
            print(f"Equipment '{related_eq_id}' does not exist in the database.")
            return "Equipment not found"

        # Create a new relationship between the exercise and equipment
        existing_exercise.related_equipment.add(existing_equipment)
        session.commit()
