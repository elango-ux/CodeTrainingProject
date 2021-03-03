class Mynum:
    # constructor it execute start along with point object
    def __init__(self, x):
        self.x = x
        
        
        
        
    # convert point object value to human readable form
    def __str__(self):
        return f"{self.x}"
    # def __iter__(self):
  
        

list = []
for i in range(1, 11):
   point = Mynum(i * 5)
   list.append(point)
iter_list = iter(list)
while True: 
    try: 
         k = iter_list.__next__()  
          
         if k % 10 == 0:
             print(k)
    except: 
        break


    



