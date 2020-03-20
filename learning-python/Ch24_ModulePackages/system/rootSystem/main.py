import sys

# path to system/ dir has to be added to PYTHONPATH to make it works
sys.path.append('/home/kamil/python-books/learning-python/Ch24_ModulePackages/system')

import system1.utils
import system2.utils

system1.utils.greet('Test1')
system2.utils.greet('Test2')