letter = ["a", "b", "c", "d", "e", "f"]
print(letter)
# access individual item in the list
print(letter[0])
# to access first item from end of list ie d
print(letter[-1])
# modify item in the list(first element in the list get modified)
letter[0] = "A"
print(letter)
#slice a string and it return array of first three item in the list
print(letter[0:3])
# it assume 0 as default and return array of first three element 
print(letter[:3])
# it list  all item in the orginal list if we did not specify end index
print(letter[0:])
# it display all item in the orginal list if we did not specify start and end index
print(letter[:])
# it delete every second element in the list
print(letter)
print(letter[::2])
numbers = list(range(20))
# it display list of numbers from  1to 19
print(numbers)
#display even number by deleting odd number in thenumber list
print(numbers[::2])
# it display all item in the  number list but in reverse order
print(numbers[::-1])
