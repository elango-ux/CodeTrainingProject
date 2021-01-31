class Point:
    def __init__(self):
        self.x = x
        self.y = y

    #magic method is used comparing value
    def __eq__(self, other):
        return self.x == other.y and self.y == other.y
    # magic method compare wheater the no is greater
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
point  =  Point(10, 20)
other  =  Point(1, 2)
print(point == other)
print(point > other)