try:     
    age = print(int(input("Age:")))
    xfactor = 10 / 0
except(ValueError, ZeroDivisionError):
     print("youdid not enter valid age")
else:
    print("no exception")