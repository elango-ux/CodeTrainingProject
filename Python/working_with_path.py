# import path class from pathlib librarey
from pathlib import Path
#path object
path = Path("elango/html_file.py")
# tocheck file existence
path.exists()
#to check path represent the file
path.is_file()
path(path.is_dir())
# it return filename in the path
print(path.name)
#it provide file name without extension
path.stem
# it return extension of file
path.suffix
#to get parent of the path
path.parent
#it help to create new path object based on existing path object but only change name and extension of file
path = path.with_name("file.txt")
#to get obsolute path
path.with_suffix(".txt")
 #to get extension of file
