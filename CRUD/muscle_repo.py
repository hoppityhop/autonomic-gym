from sqlalchemy.orm import Session
from db import SessionLocal
from models.muscle import Muscle


def create_muscle(name: str):
    """_summary_
    Create a new muscle in the database.

    Args:
        session (Session): _description_
        name (str): _description_
    """
    with SessionLocal() as session:
        # Check whether a muscle with the same name already exists
        existing_muscle = session.query(Muscle).filter_by(name=name).first()
    
        if existing_muscle:
            print(f"Muscle '{name}' already exists in the database.")
            return existing_muscle

        # Create a new Muscle object
        new_muscle = Muscle(name=name)
        # Add the muscle to the session
        session.add(new_muscle)
        # Commit the session to save the new muscle to the database
        session.commit()
        return new_muscle
