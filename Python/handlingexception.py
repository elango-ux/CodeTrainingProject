# handing exception 
try:     
    age = print(int(input("Age:")))
# as ex help detail of error message
except  ValueError as ex:
        print(ex)
        # type(ex) it show type of error
        print(type(ex))
        print("enter the age")

else:
     # this statement get executed  when error not occur
     print("no exception thrown")
# below print statement get executed  error occur or not
print("EXECUTION CONTINUE")

