# create_database.py
from sqlalchemy_utils import database_exists, create_database
from database import DATABASE_URL, engine

if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)
