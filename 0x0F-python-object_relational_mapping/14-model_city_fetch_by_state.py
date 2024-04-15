#!/usr/bin/python3

"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(mysql_username, mysql_password, database_name):
    """ Fetches all cities from the database by state """

    # Create a connection to the database
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}',
        pool_pre_ping=True
    )

    # Create a session using the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities sorted by id and join with states
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print the cities and their corresponding states in the specified format
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Read command-line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Fetch and print cities by state
    fetch_cities_by_state(mysql_username, mysql_password, database_name)

