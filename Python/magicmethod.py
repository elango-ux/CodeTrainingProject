class Point:
    # magic method it and it is calledautomatically by python interpretor depending upon how we use our object and class
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #this magical method convert object to a string
    def __str__(self):
        return f"({self.x,},{self.y})"

   # draw function inside class 
    def draw(self):
        print(f"Point({self.x}, {self.y})")
    #point object created and want to provide intial value to x and y coordinate so we need constructor
point  =  Point(1, 2)
print(point)


