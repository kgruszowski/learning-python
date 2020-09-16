from employee import Server, PizzaRobot
from customer import Customer


class Oven:
    def bake(self):
        print("oven bakes")


class Shop:
    def __init__(self):
        self.server = Server("Pat")
        self.chef = PizzaRobot("John")
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)