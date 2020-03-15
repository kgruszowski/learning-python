import module1
import module1 as module1copy  # won't copy or even load a module again, it just fetches it from already loaded modules
from module1 import b  # it'll make a copy of b from module1 to the current scope

print(dir(module1))
module1.printer('hi')

print("----------------------------------")

print(module1.b)
print(module1copy.b)
print(b)

print("----------------------------------")

module1copy.b = [1, 2, 3]  # it will change value of b in module1 as well

print(module1.b)
print(module1copy.b)
print(b)  # but b is not affected since it was copied from module1 to current scope

print("----------------------------------")

from module1 import b as b_prim

print(b)
print(b_prim)

print("----------------------------------")

print(list((key, module1.__dict__[key]) for key in module1.__dict__ if not key.startswith('__')))

print("----------------------------------")
from importlib import reload
reload(module1)
print(list((key, module1.__dict__[key]) for key in module1.__dict__ if not key.startswith('__')))