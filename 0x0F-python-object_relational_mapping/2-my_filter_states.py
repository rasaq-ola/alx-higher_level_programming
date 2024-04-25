#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Database connection
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Cursor creation
    cursor = db.cursor()

    # Executing the query with user input
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (sys.argv[4],))

    # Fetching all the results
    states = cursor.fetchall()

    # Printing results
    for state in states:
        print(state)

    # Closing cursor and database
    cursor.close()
    db.close()
