"""
Reload recursively nested modules
"""
import types
from importlib import reload


def status(module):
    print("reloading " + module.__name__)


def try_reload(module):
    try:
        reload(module)
    except:
        print("FAILED {}".format(module))


def transitive_reload(module, visited):
    if module not in visited:
        status(module)
        try_reload(module)
        visited[module] = True

        for attrobj in module.__dict__.values():
            if isinstance(attrobj, types.ModuleType):
                transitive_reload(attrobj, visited)


def reload_all(*args):
    visited = {}

    for arg in args:
        if isinstance(arg, types.ModuleType):
            transitive_reload(arg, visited)


def tester(reloader, modname):
    import importlib, sys

    if len(sys.argv) > 1:
        modname = sys.argv[1]

    module = importlib.import_module(modname)
    reloader(module)


if __name__ == '__main__':
    tester(reload_all, 'reloadall')