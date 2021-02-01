class Animals:
     
    def __init__(self):
       print("animals constructor")
       self.age = 1
   
    def eat(self):
        print("eat")
  
class Mammals(Animals):
 # intiallize weight attribute to 1
 # method in mammals class overridding base class animals so to access base class variable age
 def __init__(self):
       super().__init__()
       print("mammals constructor")
       self.weight = 1
   
 
 
 
 def walk(self):
     print("walk")

class Fish(Animals):
    def swim(self):
        print("swim")


m = Mammals()
print(m.age)
print(m.weight)