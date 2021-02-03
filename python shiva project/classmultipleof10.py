class Mynum:
    #constructor
    def __init__(self, x ):
        self.x = x
            
    def __repr__(self):  
        return " % s"% (self.x) 
    
    list = []
    def multiple(self):
        list.append(self)
        filtered = [item for item in list if item.x % 10 == 0]
        
        print(filtered)
        

list =[]
for i in  range(1, 201):
    point = Mynum(i * 5)
    point.multiple()
    
    



