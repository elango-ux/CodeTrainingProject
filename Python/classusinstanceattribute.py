class Point:
    #4)class attribute
    default_color = "red" 
    #constructor or magical method
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
   
   # draw function inside class 
    def draw(self):
        print(f"Point({self.x}, {self.y})")
     #first letterof every word is capital


# class level attribute are shared across all instances of class if you change red to yellow then it affect all point object
Point.default_color = "YELLOW"
#1)point object have default attribute x,y,z which created by constructor or whichis used by all object created
#2) we can create attribute specific to  point object
# all the attribute created x, y, z so for is called instances attribute
point.z = 10
point = Point(1, 2)
# 5)object refrence to access the default color attribute 

print(point.default_color)
# 6) POINT CLASS to access the defaultcolor attribute
print(Point.default_color)
point.draw()
# 3)another Point class object have differnt set of value both object created are independent of each other thus this is called instanceattribue
another = Point(2, 4) 
print(another.default_color)
another.draw()