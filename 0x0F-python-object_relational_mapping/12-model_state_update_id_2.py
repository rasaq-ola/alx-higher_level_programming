#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
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

    # Querying state by id
    state = session.query(State).filter(State.id == 2).first()

    # Updating state's name
    if state is not None:
        state.name = 'New Mexico'
        session.commit()

    # Closing session
    session.close()
