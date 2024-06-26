#!/usr/bin/python3

"""
Module that connects a python script to a database
"""

import sys
import MySQLdb


def city_by_state(mysql_username, mysql_password, database_name):

    connection = MySQLdb.connect(
            user=mysql_username,
            passwd=mysql_password,
            host="localhost",
            db=database_name,
            port=3306
            )

    # create a cursor objectt to interact with the database
    cursor = connection.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON states.id = cities.state_id
    ORDER BY cities.id ASC
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    # Read the arguments from the cli
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    city_by_state(mysql_username, mysql_password, database_name)
