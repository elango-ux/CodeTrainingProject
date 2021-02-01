class Product:
    def __init__(self, price):
        self.price =price
    #property decorator- when pyton interpretor see this it automatically create   property object called price 
    @property
    def price(self):
          return self.__price
    @price.setter
    def price(self, value):
        if value < 0 :
            raise ValueError("PRICE CANNOT BE negative")
        self.__price = value
    # built in property function
    price = property(get_price, set_price)
product = Product(10)
# to access the buit in property
print(product.price)


