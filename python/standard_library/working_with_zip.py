from pathlib import Path
from zipfile import ZipFile

with ZipFile(r"python\standard_library\pin.zip", "w") as zip:
    for path in Path("python\standard_library").rglob("*.*"):
        zip.write(path)

with ZipFile(r"python\standard_library\pin.zip") as zip:
    print(zip.namelist())
#zip.extractall() to extract a zip file 


