#!/usr/bin/python3

"""
Module that connects python script to a database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_containing_a(mysql_username, mysql_password, database_name):
    # Create the engine to connect to the database

    engine = create_engine(
            f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/'
            f'{database_name}',
            pool_pre_ping=True
    )

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State objects that contain the letter 'a' in their name
    states = session.query(State).filter(
            State.name.like('%a%')
            ).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    # close the session
    session.close()


if __name__ == "__main__":
    # get the arguments from the CLI

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

list_states_containing_a(mysql_username, mysql_password, database_name)
