#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Session object
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all states
    states = session.query(State).order_by(State.id).all()

    # Printing results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Closing session
    session.close()
