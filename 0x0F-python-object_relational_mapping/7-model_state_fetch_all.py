#!/usr/bin/python3

"""
This script lists all State objects from the database hbtn_0e_6_usa.
It takes three command-line arguments: mysql username, mysql password, and database name.
It uses the module SQLAlchemy and imports State and Base from model_state.
The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id and displayed as specified.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states(mysql_username, mysql_password, database_name):
    """Lists all State objects from the database hbtn_0e_6_usa."""
    # create the engine
    engine = create_engine(
                'mysql+mysqlconnector://'
                f'{mysql_username}:{mysql_password}@localhost:3306/'
                f'{database_name}',
                pool_pre_ping=True
        )
    # create a session
    session = sessionmaker(bind=engine)
    session = session()

    # Query all state obkects, ordered by state ID
    states = session.query(State).order_by(State.id).all()

    # Display the states in the format: "<state_id>: <state_name>>"
    for state in states:
        print(f"{state.id}: {state.name}")

    # close the session
    session.close()

if __name__ == "__main__":
    # get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # List all the state objects from the database
    list_states(mysql_username, mysql_password, database_name)
