#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Session object
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all cities
    cities = session.query(City).join(State).order_by(City.id).all()

    # Printing cities
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Closing session
    session.close()
