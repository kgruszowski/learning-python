class Test:
    """
    Class represents the way of mixing class and instance attributes
    """
    data = [1, 2, 3, 4]

    def __init__(self, data):
        """
        That only effects instance attribute
        """
        self.data = data

    def display(self):
        print(self.data, Test.data)

    def setClassData(self, data):
        Test.data = data


test = Test('John')
test2 = Test("Anna")
test.display()
test2.display()

test.setClassData((1, 1, 1))
test.display()
test2.display()
