#!/usr/bin/python3

"""
Script that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(mysql_username, mysql_password, database_name):
    """ Deletes all states with a name containing the letter 'a' """

    # Create a connection to the database
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/'
        f'{database_name}',
        pool_pre_ping=True
    )

    # Create a session using the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states with a name containing the letter 'a'
    states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()

    # Delete all states found
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    # Read command-line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Delete all states with a name containing the letter 'a'
    delete_states_with_a(mysql_username, mysql_password, database_name)
