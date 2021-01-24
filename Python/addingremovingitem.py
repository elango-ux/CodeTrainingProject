# to add item at end of list
letter = ["a", "b", "c", "d", "e"]
letter.append("d") 
print(letter)
# to add item  to specific place or in between
letter.insert(0, "v")
print(letter)
#to remove item at end of list
letter.pop()
print(letter)
# to remove one item  using index in the in the begining
letter.pop(0)
print(letter)
#to remove item in the list but did not know index(it remove b)
letter.remove("b")
print(letter)
# to delete range of items
del letter[0:3]
print(letter)
#to remove all item inthe list 
letter.clear()
print(letter)
