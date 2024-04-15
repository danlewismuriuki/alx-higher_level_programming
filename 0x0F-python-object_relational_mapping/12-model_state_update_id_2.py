#!/usr/bin/python3

"""
Script that changes the name of the State object with id = 2
from the database hbtn_0e_6_usa to "New Mexico".
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(mysql_username, mysql_password, database_name):
    """ Changes the name of the state with id = 2 to 'New Mexico' """

    # Create a connection to the database
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/'
        f'{database_name}',
        pool_pre_ping=True
    )

    # Create a session using the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the state with id = 2 exists
    if state_to_update:
        # Change the name of the state to 'New Mexico'
        state_to_update.name = "New Mexico"
        # Commit the transaction
        session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    # Read command-line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Update the name of the state with id = 2 to 'New Mexico'
    update_state_name(mysql_username, mysql_password, database_name)
