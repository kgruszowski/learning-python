import re

def greet(msg):
    print(msg + " Hello from system3!")
    print("This is re module from system3 (absolute import although local module with the same name exists)", dir(re))