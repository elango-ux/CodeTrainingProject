try:
    #open a file this return file object
    file = open("app.py")
    age = int(input("age:"))
    xfactor = 10 / age
except(ValueError, ZeroDivisionError):
    print("no exception were thrown")
# finally statement get executed always even though it throw exception or not
finally:
       # it close open file
       file.close("app.py")

