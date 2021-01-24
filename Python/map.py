item = [
         ("product1", 10),
         ("product2", 9),
         ("product1", 12),

]
#map function
# iterate over tuple inside list and display all tuples
price = []
for items in item:
    print(items)
    # it append item in the price=[] list
    price.append(items[1])
    #map of price in the item list
    print(price)
#map fuuntion
    x = map(lambda item1: items[0], item)
# map function return another object which is another iterable
    print(x)
    for item2 in x:
        print(item2)