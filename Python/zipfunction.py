# zip function combine  two list ormore list
list1 = [2,3,4,4,5]
list2 = [3,4,2,4,5]
#print statment return zip object which is iterable
print(zip(list1, list2))
# print function use list fuction to convert zip object to tuple of  combined list1 and list2
print(list(zip(list1, list2)))
# now pass string "abc" inside zip  it combine with list 1  nd list 2
print(list(zip(list1, list2,"abc")))