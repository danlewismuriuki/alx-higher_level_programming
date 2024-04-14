#!/usr/bin/python3

"""
Module that connects python script to a database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_my_get(
        mysql_username,
        mysql_password,
        database_name,
        state_name
        ):
    """ Fetches the state object with the given name from the
    database and prints its ID
    """
    # Create a connection with the database
    engine = create_engine(
            f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/'
            f'{database_name}',
            pool_pre_ping=True
    )

    # Create a session using the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the ID of the state if found, else print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Read command-line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    # Fetch and print the state by name
    model_state_my_get(
            mysql_username,
            mysql_password,
            database_name,
            state_name
            )
