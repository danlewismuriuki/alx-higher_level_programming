#!/usr/bin/python3

"""
Module that connects python script to a database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state_louisiana(mysql_username, mysql_password, database_name):
    """ Adds the state object "Louisiana" to the database and prints its ID """
    # Create a connection to the database

    engine = create_engine(
            f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/'
            f'{database_name}',
            pool_pre_ping=True
            )
    # Create a session using the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object with the name "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new state to the session and commit the transaction
    session.add(new_state)
    session.commit()

    # Print the new state's ID after creation
    print(new_state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    # Read command-line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Add the state "Louisiana" to the database and print the new state's ID
    add_state_louisiana(mysql_username, mysql_password, database_name)
