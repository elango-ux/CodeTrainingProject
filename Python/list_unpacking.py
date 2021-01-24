# access individual element in the list can be done list unpacking
number = [1,2,3]
# listunpacking
first, second, third = number
print(second)
numbers =[1, 2, 2, 4, 4,3]
#there are so many item in the list but  need to access first two element in the list

first, second, *other = numbers
# *other packing remaining element in the second list
print(first, second, other)
#to get first and last item in the list numbers
first, *other, last = numbers
print(first, other, last)


