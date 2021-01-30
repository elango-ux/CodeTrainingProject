# create empty list
list = []
#list comprehension 
multipleoffive = [item * 5 for item in range(0, 5000)]
# add item to the list
list.append(multipleoffive)
#display multiple of 5
print(list)
#loop through list
for items in range(len(list)):
    #list comprehesion do filter operation 
    filtered = [item1 for item1 in list[items] if(item1 % 10 == 0)] 
    # display multiple of 10 in the list
    print(filtered)
       
    
    