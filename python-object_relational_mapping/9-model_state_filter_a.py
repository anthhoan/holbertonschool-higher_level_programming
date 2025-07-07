#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a'
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
    for letter_a in session.query(State).order_by(State.id)\
            .filter(State.name.contains('a')).all():
        print("{}: {}".format(letter_a.id, letter_a.name))
        """Using the session with SQLAlchemy"""
    session.close()
    """Closing the session"""
