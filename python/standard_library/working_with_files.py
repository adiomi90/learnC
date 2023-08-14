from pathlib import Path

#from time import ctime

#path = Path(r"C:\Users\max\OneDrive\alx\c\learnC\python\standard_library\working_with_files.py")
#print(path.exists())
#print(ctime(path.stat().st_ctime))

#print(path.read_text())


#with open("filename.py" , "r") as file
#...

source = Path(r"python/standard_library/directory.py")
targety = Path(r"python/standard_library/")/ "__init__.py"

targety.write_text(source.read_text())
targety.unlink()