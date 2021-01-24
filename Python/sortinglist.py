numbers = [3, 4, 5, 6, 7,2]
# to sort ascending order
numbers.sort()
print(numbers)
# to sort in descending order
numbers.sort(reverse = True)
print(numbers)
# sorted buit in function used for iterable to display ascending order and it create newlist
print(sorted(numbers))
# sorted built in function to reverse number and number is iterable
print(sorted(numbers,reverse = True))
# arrange array of tuples in the list based on price
item = [
         ("product1", 10),
         ("product2", 9),
         ("product1", 12),

]
print(item)
def sort_item(item):
    # to acess the price in tuples
    return item[1]
item.sort(key=sort_item)
print(item)
