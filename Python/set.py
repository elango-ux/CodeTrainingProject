numbers = [1, 2, 3, 4, 3, 1]
unique = set(numbers)
# set function return object consists of unique value and list is converted to set
print(unique)
# add new item
second = {1, 4 }
second.add(5)
print(second)
#remove new item
second.remove(5)
# length of set
len(second)
# union of two set
union = unique | second
print(union)
 # intersection of  two set using  &
intersection = unique & second
print(intersection)
#differnce between two set  using -
differnce = unique - second
print(differnce) 
# it  return items in first or second  but not return item it present in both
print(unique ^ second)
#existence of item in the set using in operation
if 10 in unique:
    print("existed")