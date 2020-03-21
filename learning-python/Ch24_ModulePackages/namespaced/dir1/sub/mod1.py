# relative imports works in namespace as well
from . import mod2

print("dir1/sub/mod1")

# call function from mod2 module placed in the same namespace but another directory
mod2.testMod2()