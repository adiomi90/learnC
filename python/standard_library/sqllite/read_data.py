import sqlite3
from pathlib import Path
import json 

with sqlite3.connect(r"python\standard_library\sqllite\inkbaby.db") as conn:
    command = "SELECT * from Movies"
    cursor = conn.execute(command)
    """ for row in cursor:
        print(row) """
    movies = cursor.fetchall()
    print(movies)