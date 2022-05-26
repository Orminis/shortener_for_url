# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

# You can think of engine as the entry point to your database.
engine = create_engine(
    get_settings().db_url, connect_args={"check_same_thread": False}
    # With this connection argument, SQLite allows more than one request at a time to communicate with the database.
)

"""You use sessionmaker, which you import in line 5, to create the SessionLocal class in line 12.
   You’ll create a working database session when you instantiate SessionLocal later."""
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

"""The declarative_base function that you import in line 4 returns a class that connects the database engine
to the SQLAlchemy functionality of the models.
Base will be the class that the database model inherits from in your models.py file."""
Base = declarative_base()
