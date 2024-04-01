#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database hbtn_0e_6_usa."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy.orm.exc import NoResultFound
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(State.name == state_name).one()
        print("{}".format(state.id))
    except NoResultFound:
        print("Not found")

    session.close()
