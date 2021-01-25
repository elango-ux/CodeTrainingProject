#array
# import array class in array module
from array import array
numbers = array("i", [1, 2, 3])

numbers.append(7)
# addnumbers to begining of array
print(numbers)
numbers.pop()
# delete last number in thearray
print(numbers)
numbers.insert(2,23)
#insert numbers
print(numbers)