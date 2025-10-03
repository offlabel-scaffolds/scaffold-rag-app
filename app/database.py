from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)