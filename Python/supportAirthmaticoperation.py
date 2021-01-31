class Point:
    # magic method it and it is calledautomatically by python interpretor depending upon how we use our object and class
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #magical method perform addtion of two object
    def __add__(self,other):
        return Point(self.x + other.x,self.y + other.y) 

    
    
    
point  =  Point(10, 20)
other  =  Point(1, 2)
# it return object because we removed __str__ so we used combined.x  two add two value
combined = point + other
print(combined.x)