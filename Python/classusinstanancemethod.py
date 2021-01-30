class Point:
     #1) method defined inside class is calledinstaneous method and can be accesed sing instnceous object
    def __init__(self, x, y):
        self.x = x
        self.y = y
   # 6)@classmethod is called as decorator is a class method
    @classmethod
    #5)cls = short for calss and cls refernce to class
    def zero(cls):
        #cls(0, 0) it create point object with intial value.when it see cls python interpretor send refernce to Point 
        return cls(0, 0)

   # 2)draw function inside class  is instance method
    def draw(self):
        print(f"Point({self.x}, {self.y})")
    #point object created and want to provide intial value to x and y coordinate so we need constructor
# 4) zero is method that defined in class level when we call using point object and it return a value.in this example zero method is a factory method because it create new object
point = Point.zero()
#3)instaneous object acess draw method
# when we call this function it return 0,0
point.draw()

