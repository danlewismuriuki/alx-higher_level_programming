#!/usr/bin/python3

"""
This module has a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_us

"""

import MySQLdb
import sys


def filter_cities(mysql_username, mysql_password, database_name, state_name):
    # Connect to the MySQL database using th eprovided credentials
    connection_todb = MySQLdb.connect(
            user=mysql_username,
            host="localhost",
            db=database_name,
            passwd=mysql_password,
            port=3306
            )

    cursor = connection_todb.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    param = (state_name,)
    cursor.execute(query, param)

    rows = cursor.fetchall()

    city_names = []

    for row in rows:
        city_names.append(row[0])

    print(", ".join(city_names))

    # close the cursor
    cursor.close()

    # close the data base
    connection_todb.close()


if __name__ == "__main__":
    # Get arguments from the cli
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities(mysql_username, mysql_password, database_name, state_name)
