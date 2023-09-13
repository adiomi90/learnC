#!/usr/bin/python

import sys
import MySQLdb

"""This script lists all the cities """

def list_all_cities():
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <dbname>")
        return
    
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306
   
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
        cur = db.cursor()
        cur.execute("select c.id, c.name, s.name  from cities as c join states as s on c.state_id = s.id order by c.id")
        result = cur.fetchall()
    

        for row in result:
            print(row)

        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_all_cities()