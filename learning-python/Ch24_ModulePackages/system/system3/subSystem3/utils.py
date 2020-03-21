from .. import re
import string

def greet(msg):
    print(msg + " Hello from subSystem3!")
    print("Re module called relatively from subpackage of system3", dir(re))
    print("Import absolute string module - it will load string module from rootSystem dir", dir(string))
