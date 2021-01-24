item = [
         ("product1", 10),
         ("product2", 9),
         ("product1", 12),

]
item.sort(key=lambda item: item[1])
print(item)