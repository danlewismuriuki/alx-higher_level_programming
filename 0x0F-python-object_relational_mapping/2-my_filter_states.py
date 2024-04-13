#!/usr/bin/python3
"""
This module connects a python script to a MYSQL dtabase and displays values
from the states table where name matches a given argument
"""

import sys
import MySQLdb


def display_values(mysql_username, mysql_password, database_name, state_name):
    connect = MySQLdb.Connection(
            user=mysql_username,
            passwd=mysql_password,
            host="localhost",
            db=database_name,
            port=3306
            )


    cursor = connect.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connect.close()


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    display_values(mysql_username, mysql_password, database_name, state_name)
