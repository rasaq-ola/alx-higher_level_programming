#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")
    for city in cursor.fetchall():
        print(city)
    cursor.close()
    db.close()
