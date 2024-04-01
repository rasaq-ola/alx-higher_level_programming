#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database hbtn_0e_6_usa."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    new_state_name = 'Louisiana'

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name=new_state_name)
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
