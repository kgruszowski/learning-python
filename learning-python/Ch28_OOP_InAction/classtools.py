class AttrDisplay:
    """
    Provides an inheritable display overload method that shows instances with their class names
    and a name=value pair for each attribute from instance but not inherited from class
    """
    def gather_attrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('{}={}'.format(key, getattr(self, key)))

        return ', '.join(attrs)

    def __repr__(self):
        return '[{}: {}]'.format(self.__class__.__name__, self.gather_attrs())


if __name__ == "__main__":
    class TopTest(AttrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()

    print(X)
    print(Y)