class Animals:
    # inherite attribute from animals class
    def __init__(self):
       self.age = 1
   
    def eat(self):
        print("eat")
#Mammals class inerits Animals 
# Animals class is baseclass andmamamals class is child   
class Mammals(Animals):
 def walk(self):
     print("walk")
#fish classinheritece from Animals class
class Fish(Animals):
    def swim(self):
        print("swim")


m = Mammals()
m.eat()
#inherite age attribute from animals class
print(m.age)