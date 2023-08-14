from pathlib import Path
import json

""" movies = [
    {"id":1, "title":"Particles", "year":1990},
    {"id":2, "title":"Par", "year":1992},
    {"id":3, "title":"The Ink", "year":1993},
    {"id":4, "title":"Molecular", "year":1994}
]

movies_path = Path(r"python\standard_library\sqllite\particles.json")
movies_path.write_text(json.dumps(movies)) """

movies = json.loads(Path(r"python\standard_library\sqllite\particles.json").read_text())
for movie in movies:
    print(movie)