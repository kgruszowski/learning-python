"""
That module show the way we could implement inheritance in Python
"""


class Super:
    """
    Base class for our example
    """

    def method(self):
        print('in Super.method')

    def delegate(self):
        self.action()  # action to be defined


class Inheritor(Super):
    """
    Inherits everything from Super
    """
    pass


class Replacer(Super):
    """
    Replace method completely
    """

    def method(self):
        print('in Replacer.method')


class Extender(Super):
    """
    Add own logic to base implementation
    """

    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):
    """
    Fill in a required method
    """

    def action(self):
        print("in Provider.action")


if __name__ == "__main__":
    for class_name in (Inheritor, Replacer, Extender):
        print('\n' + class_name.__name__ + "...")
        class_name().method()

    print('\nProvider...')
    x = Provider()
    x.delegate()
