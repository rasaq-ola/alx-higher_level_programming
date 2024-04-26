#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    # Fetching all the results
    cities = cursor.fetchall()
    # Printing results
    for city in cities:
        print(city)
    # Closing cursor and database
    cursor.close()
    db.close()
