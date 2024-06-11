#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
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

    # Querying state by name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Printing result
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Closing session
    session.close()
