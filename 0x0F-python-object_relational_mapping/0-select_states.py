#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
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

    # Executing the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all the results
    states = cursor.fetchall()

    # Printing results
    for state in states:
        print(state)

    # Closing cursor and database
    cursor.close()
    db.close()
