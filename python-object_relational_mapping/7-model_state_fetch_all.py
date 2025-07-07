#!/usr/bin/python3
"""List all State objects from the database hbtn_0e_6_usa with SQLAlchemy"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                    .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    """create the engine"""
    """pool_pre_ping=True tests the database connections before continuing"""
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    """connecting to the session"""
    for state in session.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))
    session.close()
    """close the session"""
