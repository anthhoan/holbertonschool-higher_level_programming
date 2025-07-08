#!/usr/bin/python3
"""Adds the State object 'Louisiana'
to the database hbtn_0e_6_usa with SQLAlchemy"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    """Connect to the database"""
    Base.metadata.create_all(engine)
    """Create tables if they don't exist"""
    Session = sessionmaker(bind=engine)
    """Create session factory"""
    session = Session()
    """Create actual session"""
    new_state = State(name ="Louisiana")
    """Using the session with SQLAlchemy"""
    session.add(new_state)
    """Adding a new object to the database"""
    session.commit()
    """Pushing changes to the database"""
    print(new_state.id)
    session.close()
    """Closing the session"""
