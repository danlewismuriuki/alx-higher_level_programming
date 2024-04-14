#!/usr/bin/python3

"""
This script lists all State objects from the database hbtn_0e_6_usa.
It takes three command-line arguments: mysql username, mysql password,
and database name.
It uses the module SQLAlchemy and imports State and Base from model_state.
The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and displayed as specified.
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def model_state_fetch_all(mysql_username, mysql_password, database_name):
    """ Lists all state objects from the database hbtn_0e_6_usa."""

    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/'
        f'{database_name}',
        pool_pre_ping=True
    )

    # create a session using the engine
    session = sessionmaker(bind=engine)
    session = session()

    # Display the states in the format: "<state_id>:"
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    # Retrive commands from the cli
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    model_state_fetch_all(
            mysql_username,
            mysql_password,
            database_name
            )
