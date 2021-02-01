class Animals:
    def eat(self):
        print("eat")
#Mammals class inerits Animals 
# Animals class is baseclass andmamamals class is child   


class Mammals(Animals):
 def walk(self):
     print("walk")

m = Mammals()
# it check m obect is instances of class Mammals
print(isinstance(m, Mammals))
# Mammals inherite from Animals so m object is instances of Animals class
print(isinstance(m, Animals))
#object class is base class for all class in python
print(isinstance(m, object))
# it check mammals class is subclass of animals
print(issubclass(Mammals,Animals))