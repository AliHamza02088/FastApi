from sqlalchemy import create_engine  #create_engine is used to create a new database engine
from sqlalchemy.ext.declarative import declarative_base  #declarative_base is used to create a new base class for the models
from sqlalchemy.orm import sessionmaker #sessionmaker is used to create a new session class for the database

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"  # SQLite database file

engine = create_engine(SQLALCHEMY_DATABASE_URL , connect_args={"check_same_thread": False},)  # create_engine is used to create a new database engine with the specified URL and connection arguments

# Create a new session class
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

#Base is export to models to make new model classes 
Base = declarative_base()  #create a new base class for the models.

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()