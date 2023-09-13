#!/usr/bin/python3

import sys
import MySQLdb

user = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]
localhost = "localhost"
port = 3306

try:
    if (len(sys.argv) != 4):
        print("Need 4 arguments")

    db = MySQLdb.connect(localhost, user, password, db_name, port)
    con = db.cursor()
    con.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""") #binary makes it case sensitive
    result = con.fetchall()

    for row in result:
        print(row)

    con.close()
    db.close()

except MySQLdb.Error as e:
    print(f"Error {e}")