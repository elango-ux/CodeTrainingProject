class Animals:
     
    def eat(self):
        print("eat")
  
class Bird(Animals):
    def fly(self):
      print("fly")

# chicken inherte all instance of bird class but chicken could not fly
class Chicken(Bird):
    pass


