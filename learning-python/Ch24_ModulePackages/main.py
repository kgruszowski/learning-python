import dir1.dir2.mod

# won't load package again
import dir1

# unless you reload it
from importlib import reload
reload(dir1)

# it also reload subpackage without its parent
reload(dir1.dir2)  # only dir2/__init__.py will be called

# you can access dir2 as a field in dir1
print(dir1.dir2)

# now let's play with variables from __init__ files
print(dir1.x, dir1.dir2.y, dir1.dir2.mod.z)

# it is a little bit annoying let's use from
# worth to mention that it also runs __init__ files
from dir1.dir2 import mod
print(mod.z)