#!/usr/bin/python3
"""
This module connects a python script to a databse
"""

import sys
import MySQLdb


def city_list(mysql_username, mysql_password, database_name):

    connection = MySQLdb.connect(
            user=mysql_username,
            host="localhost",
            passwd=mysql_password,
            port=3306,
            db=database_name
            )

    # create a cursor object to interact with the database
    cursor = connection.cursor()

    query = "SELECT * FROM states ORDER BY states.id ASC;"

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

    city_list(mysql_username, mysql_password, database_name)
