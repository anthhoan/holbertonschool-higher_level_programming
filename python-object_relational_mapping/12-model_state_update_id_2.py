#!/usr/bin/python3
"""SCript that changes the name of a State object
from the database hbtn_0e_6_usa"""
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
    state_update = session.query(State).filter_by(id='2').first()
    if state_update:
        state_update.name = "New Mexico"
        """Using the session with SQLAlchemy"""
    session.commit()
    """Pushing changes to the database"""
    session.close()
    """Closing the session"""
