# map the  price of the product
item = [
         ("product1", 10),
         ("product2", 9),
         ("product1", 12),

]
# list comprehension used to map the price of the product
price = [items[1] for items in item ]
print(price)
#filter price using list comprehension
filtered = [items for items in item if items[1] >= 10]
print(filtered)