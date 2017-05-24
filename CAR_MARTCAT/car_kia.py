class Car:

    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color

class Car_company(Car):
    def __init__(self,name,price,color,brand):
        Car.__init__(self,name,price,color)
        self.brand = brand