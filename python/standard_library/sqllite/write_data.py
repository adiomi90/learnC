import sqlite3
from pathlib import Path
import json 

movies = json.loads(Path(r"python\standard_library\sqllite\particles.json").read_text())

with sqlite3.connect(r"python\standard_library\sqllite\inkbaby.db") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()