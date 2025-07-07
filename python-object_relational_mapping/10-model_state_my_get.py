#!/usr/bin/python3
"""Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa using SQLAlchemy"""
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
    get_state = session.query(State).order_by(State.id)\
            .filter(State.name == sys.argv[4]).first()
    if get_state is None:
        print("Not Found")
    else:
        print("{}".format(get_state.id))
    """Using the session with SQLAlchemy"""
    session.close()
    """Closing the session"""
