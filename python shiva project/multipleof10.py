# create empty list
list = []
#list comprehension 
multipleoffive = [item  for item in range(1, 5001)]
# add item to the list5
list.append(multipleoffive)
#display multiple of 5
for i in range(len(list)):
    filtered = [item1  for item1 in list[i] if(item1 % 5 == 0)]
    # print(filtered) 
    filtered1 = [item2 for item2 in list[i] if(item2 % 10 == 0)]
    print(filtered1)  
    












    #loop through list
#  for items in range(len(list)):
    # list comprehesion do filter operation 
    # filtered = [item1 for item1 in list[items] if(item1 % 10 == 0)] 
    # display multiple of 10 in the list
    # print(filtered)
       