# display even number using list comprehension
evennumber = [x * 2 for x in range(10)]
print(evennumber)
# generator object or expression take less memory
values = (x * 2 for x in range(10))
#it show output generator object so we shold loop to get output 
print(values)
for x in values:
    print(x)
# get siz of generator expression
from  sys import  getsizeof
values = ( x * 2 for x in range(1000))
# getsizeof class provide size of values 
print("gen:", getsizeof(values))