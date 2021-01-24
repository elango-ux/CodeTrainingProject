
letters = ["a", "b", "c", "d", "e"]
#loop over list
#enumerate(iterable) it return tuple contain index and value of list  
for number in enumerate(letters):
    print(number)
    #to access index  in tuple 
    print("it dispaly all index of item",number[0])
    # to acess item in tle list
    print(number[1])