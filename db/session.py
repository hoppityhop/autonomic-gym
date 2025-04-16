from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from secret import password

DATABASE_URL = "mysql://root:"+password+"@localhost:3306/gymdb"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
