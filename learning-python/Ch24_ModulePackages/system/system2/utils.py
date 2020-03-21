from . import re

def greet(msg):
    print(msg + " Hello from system2!")
    print("This is re module from system2 (relative import)", dir(re))