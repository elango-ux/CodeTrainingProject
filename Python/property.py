class Product:
    def __int__(self, price):
        self.price = price
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be negative")
        self.__price = value

    price = property(price,price)
     
product = Product(-50)
product = Product(10)
print(product.price)
