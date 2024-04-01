#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table
   of hbtn_0e_0_usa where name matches the argument, safe from MySQL injection"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
