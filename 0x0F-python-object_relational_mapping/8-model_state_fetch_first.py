#!/usr/bin/python3

"""
Module that connects python script to a database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state(mysql_username, mysql_password, database_name):
    """ Fetches the first state object from the database and prints it """

    # create a connection with the databse
    engine = create_engine(
            f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/'
            f'{database_name}',
            pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    Session = Session()

    # Query the first state ordered by states.id
    first_state = Session.query(State).order_by(State.id).first()

    # Query the first state ordered by states.id
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # close the session
    Session.close()

if __name__ == "__main__":
    # read command line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Fetch and print the first state
    fetch_first_state(mysql_username, mysql_password, database_name)
