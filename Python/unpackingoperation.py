# how to get individual value like this 1,2,3 to get prefix with unpacking operators * 
numbers = [1, 2, 3] 
# * upacking operator remove the container and it take individual element and pass them in arbitary argument in print function
print(*numbers)
# bracket create list 
values = [*range(5),*"hello"]
print(values)
#combine two list using *
list1 = [1, 3, 4, 5, 5,]
list2 = [23, 23, 22, 44,32]
combinedlist = [*list1, "a",*list2, "A"]
print(combinedlist)
# UNPACKING operator * is used to combine dictionary
first = {"x": 1, "y":3}
second = {"x":1, "y":2,"z":32}
# **operator take all the key value pair in first and second dictionary
combinedictionary = {**first, **second, "k":43}
print(combinedictionary)
  