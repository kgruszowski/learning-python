class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, "order from ", server)

    def pay(self, server):
        print(self.name, "pays for item to", server)