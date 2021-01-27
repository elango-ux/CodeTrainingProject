try:
    #instead of getting return value of open statemen  we  prefixed with statement and to acess to  return value of openfunction we use as file 
    # with statement automatically relese external file without finally block
    with open("app.py") as file: 
        age = int(input("age:"))
    xfactor = 10 / age
except(ValueError, ZeroDivisionError):
     print("no exception were thrown")
else:
    print("No exception were thrown")
    