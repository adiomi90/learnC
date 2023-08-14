from pathlib import Path

path = Path("python\standard_library")
""" print(path)
print(path.exists())
path.mkdir()
path.rmdir()
path.rename("\name")
 """
# for p in path.iterdir():
#     print(p)

paths = [p for p in path.iterdir()]
#this is used to search for using a pathe
py_files =[p for p in  path.rglob("*.py")]
print(py_files)