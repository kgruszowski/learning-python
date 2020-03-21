import sys

# path to system/ dir has to be added to PYTHONPATH to make it works
sys.path.append('/home/kamil/python-books/learning-python/Ch24_ModulePackages/system')

import system1.utils
import system2.utils
import system3.utils
import system3.subSystem3.utils

system1.utils.greet('Test1')
system2.utils.greet('Test2')
system3.utils.greet('Test3')
system3.subSystem3.utils.greet('Test3Subsystem')