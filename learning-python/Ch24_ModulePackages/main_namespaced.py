import sys

# to make namespace works add both location to PYTHONPATH
# namespaces does not require __init__.py files since there is a special algorithm which finds modules in a namespace
sys.path.append('/home/kamil/python-books/learning-python/Ch24_ModulePackages/namespaced/dir1')
sys.path.append('/home/kamil/python-books/learning-python/Ch24_ModulePackages/namespaced/dir2')

import sub

print(sub)
print(sub.__path__)

# during import files are scanned and code is run top-bottom
from sub import mod1
from sub import mod2

print(mod1)
print(mod2)