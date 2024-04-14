#!/usr/bin/python3

"""
Module that defines a state class and a Base instance for SQLALchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """
    State class that links to MySQL table `states`
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # To create the `states` table column id

    def create_state_table(mysql_username, mysql_password, database_name):
        # create the engine
        engine = create_engine(
                'mysql+mysqlconnector://'
                f'{mysql_username}:{mysql_password}@localhost:3306/'
                f'{database_name}',
                pool_pre_ping=True
        )

        # create the `state` table in the database
        Base.metadata.create_all(engine)


# If the script is executed directly, create the table
if __name__ == "__main__":

    import sys

    # Read command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the `states` table
    create_state_table(mysql_username, mysql_password, database_name)
