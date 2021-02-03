from pathlib import Path

#path object for directories
path = Path("elango")
path.exist()
#create directories
path.mkdir()
#remove directory
path.rmdir()
#rename
print(path.rename("elango2"))
#we can get list of directries and files in the path 
print(path.iterdir())