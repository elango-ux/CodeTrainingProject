point = (1, 2) + (3, 4)
# concatenate tuple
print(point)
# repeat a tuple using multiplication operator
point = (1, 2)*3
print(point)
#convert list to tuple
list = [1, 2, 3, 4]
list1 = tuple([1, 2, 3, 4])
print(list1)
#accessing individual items
point =(1, 2, 3)
print(point[0])
# to get range of items
point = (1, 2, 3)
print(point[0:2])
#unpacking of tuple
point = (1, 2, 4)
num, num2, num3 = point
print(num, num2, num3)
# in operator to check existenceof item
point = (1, 3, 4)
if  3 in point:
    print("existed")

