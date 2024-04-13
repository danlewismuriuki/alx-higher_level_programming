#!/usr/bin/python3
"""
This module connects to a MySQL database and displays all values
in the `states` table where the name matches a given argument.
"""

import sys
import MySQLdb


def display_values(mysql_username, mysql_password, database_name, state_name):
    # Establish a connection to the MySQL database
    connection = MySQLdb.connect(
        user=mysql_username,
        passwd=mysql_password,
        host="localhost",
        db=database_name,
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Create the query using format() to insert user input safely
    query = "SELECT *
    FROM states
    WHERE name = '{}'
    ORDER BY id ASC".format(state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch all rows that match the query
    rows = cursor.fetchall()

    # Iterate through rows and print each row
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    # Read the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the display_values function with the provided arguments
    display_values(mysql_username, mysql_password, database_name, state_name)
