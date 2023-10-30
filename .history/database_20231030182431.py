from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
DATABASE_URL = "postgresql://postgres:20168692!@localhost/product"

database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db= Sessionlocal ()
    try:
        yield db
    finally:
        db.close()