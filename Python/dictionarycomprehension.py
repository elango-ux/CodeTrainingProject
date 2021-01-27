# loop using range and add item in the list using append function
values = []
for x in range(6):
    values.append(x * 2)
print(values)
#use map function or list comprehension  to loop over it add item in the list 
values = [x * 2 for x in range(5)]
print(values)
# you can use list comprehension in  to add value in set
values = {x * 2 for x in range(5)}
print (values)
# you use list comprehension for dictionary  to loop over display key and value inside dictionry(in program expression x represent key  and x *2 represent value)
values = {x: x * 2 for x in range(5)}
print(values)
values = {}
#to add key value pair in the dictionary using loop
for x in range(5):
    values["x"] = x * 2
print(values)
# tuples- it  display in the screen   generate object while printing(next topic)
values = (x *2 for x in range(6))
print(values) 



