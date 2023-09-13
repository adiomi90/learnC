#!/usr/bin/python3

import MySQLdb
import sys

def secure_fetch():
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    localhost = "localhost"
    port = 3306

    db = MySQLdb.Connect(host=localhost, user=user,
                          passwd=password, db=db_name, port=port)
    cur = db.cursor()
    cur.execute("Select * from states where name Like %s order by id Asc", [state_name])

    result = cur.fetchall()

    for row in result:
        print(row)

if __name__ == "__main__":
    secure_fetch()
