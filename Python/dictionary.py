#dictionary
point = {"x": 1, "y": 2, "z": 3 }
# dict() function is used to create  dictionary
point = dict(x = 1, y =2, z = 3,)
print(point["x"])
# modify the value x  to new value
modify = point["x"] = 10
print(modify)
# add a  new  key
addkey = point["h"] = 20
print(addkey)
# to check existence of key
if "z" in point:
    print(point["z"])
#other method to check existence of key  and 0 is default value and  return if key does not exist
print(point.get("a", 0))
#delete an item
del point["x"]
print(point)
# loop over dictionary. each iteration it hold key of the item
for key in  point:
    #it teturn every key in the dictionary
    print(key)
    # to take value in the dictionary you use dictionary name[key]
    print(point[key])
#other way to  iterate over dictionary
for key, value in point.items():
    # point.item convert dictionary keyvalue pair to tuple("h",20)
    print(value)
    # to take key and value  in the tuple so you unpack it
    print(key, value)


       
