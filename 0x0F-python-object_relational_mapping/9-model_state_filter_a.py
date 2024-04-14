#!/usr/bin/python3

"""
Script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
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

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects that contain the letter 'a' in their
    # name and sort by State.id
    states_with_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


# Ensure the script is not executed when imported
if __name__ == "__main__":
    # Get the MySQL username, password, and database name
    # from command-line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Call the function to list states containing the letter 'a'
    list_states_containing_a(mysql_username, mysql_password, database_name)
