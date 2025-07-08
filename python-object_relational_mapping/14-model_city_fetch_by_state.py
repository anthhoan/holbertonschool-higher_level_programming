#!/usr/bin/python3
"""List all State objects from the database hbtn_0e_6_usa with SQLAlchemy"""
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    """Connect to the database"""
    Base.metadata.create_all(engine)
    """Create tables if they don't exist"""
    Session = sessionmaker(bind=engine)
    """Create session factory"""
    session = Session()
    """Create actual session"""
    results = session.query(State, City).join(City, State.id == City.state_id)\
        .order_by(State.id, City.id).all()
    for state, cities in results:
        print("{}: ({}) {}".format(state.name, cities.id, cities.name))
    """Using the session with SQLAlchemy"""
    session.close()
    """Closing the session"""
