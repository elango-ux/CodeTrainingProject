class Mynum:
    def __init__(self, x ):
        self.x = x
        
    def __repr__(self):  
        return " % s"% (self.x) 

    def multiple(self):
        print(self.x)
        

list =[]
for i in  range(1001):
    point = Mynum(i * 5)
    list.append(point)

for items in range(len(list)):
    #list comprehesion do filter operation 
    filtered = [item1 for item1 in list[items] if(item1 % 10 == 0)] 
    # display multiple of 10 in the list
    print(filtered)
       
    



