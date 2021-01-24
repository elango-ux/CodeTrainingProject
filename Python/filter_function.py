item = [
         ("product1", 10),
         ("product2", 9),
         ("product1", 12),

]
x = list(filter(lambda item: item[1] >= 10, item ))
print(x)