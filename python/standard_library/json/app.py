import json
from pathlib import Path

""" movies = [
    {"id":1,"name":"particles", "year":1960},
    {"id":2,"name":"done", "year":1968},
    {"id":3,"name":"sanri", "year":1969},
    {"id":4,"name":"ink kila", "year":1970},
]

data = json.dumps(movies)
Path(r"python\standard_library\particles.json").write_text(data)
 """
result = Path(r"python\standard_library\particles.json").read_text()
movies = json.loads(result)
print(movies[0])
