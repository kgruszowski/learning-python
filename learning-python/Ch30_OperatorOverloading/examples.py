class Arr:

    arr = []

    def __init__(self, arr):
        self.arr = arr

    def __getitem__(self, item):
        return self.arr[item]


a = Arr([10,20,30,40,50,60])
print(a[2])

class PowerArr:
    arr = [1,2]

    def __setitem__(self, key, value):
        self.arr[key] = value**2

    def __str__(self):
        return str(self.arr)

# it works because it passes slice() object
print(a[:2])
print(a[slice(0,2)])

b = PowerArr()
b[0] = 10
b[1] = 5

print(b)

class SquareRange:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration

        self.value += 1

        return self.value**2

for num in SquareRange(10,15):
    print(num, end=' ')

Y = SquareRange(1,5)
print()
print([n for n in Y])
print([n for n in Y]) # we return the same value on __iter__ so it's a one-shot iter


class Blackbox:
    def __getattr__(self, item):
        if item == 'foo':
            return item * 3
        elif item == 'bar':
            return item[::-1]
        else:
            raise AttributeError(item)

box = Blackbox()
print(box.foo)
print(box.bar)


class PowerAdder:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return self.data ** 2 + other.data ** 2

    def __radd__(self, other):
        return self.data ** 2 + other ** 2


p1 = PowerAdder(2)
p2 = PowerAdder(4)
print(p1 + p2) # should be 4 + 16 = 20 - trigger __add__
print(10 + p1) # trigger __radd__

class LivePrompter():
    def __init__(self, name):
        print("Hello {}".format(name))
        self.name = name

    def do_something(self):
        print("{} is doing something".format(self.name))

    def __del__(self):
        print("Hey {} time to die".format(self.name))


jake = LivePrompter("Jake")
jake.do_something()
jake = LivePrompter("Jake clone")
jake.do_something()
jake = "test"
