#first letterof every word is capital
class Point:
    # 2)magical method otherwise called constructor
       
    def __init__(self, x, y):
        #self point to current object so you can access the attribute using self.x and set value 
        self.x = x
        self.y = y
   
   
   # draw function inside class 
    def draw(self):
       
        print(f"Point({self.x}, {self.y})")
    # 1)point object created and want to provide intial value to x and y coordinate so we need constructor to achive this

    def draw1(self):
        print(self.x)


point = Point(1, 2)
# draw method inside class is accesed using dot notation
point.draw()
point.draw1()
