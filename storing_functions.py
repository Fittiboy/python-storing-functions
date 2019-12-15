import json
import os
from function_body import function_body as funcbod

# Helper function
def get_funclist():
    with open('functions\\functions.list') as funclist_file:
        funclist = json.load(funclist_file)
    return funclist

# Helper function
def store_funclist(list):
    with open('functions\\functions.list', 'w') as funclist_file:
        json.dump(list, funclist_file)

def store(name):
    """Stores a function with the name "on_name" in the "functions" directory.
    The body of the function is defined in "function_body.py".
    the "on_" prefix is used to easily find the functions later, after
    they've been imported"""
    with open(f'functions\\on_{name}.py', 'w') as function:
        function.write(f'def on_{name}():\n')
        body = funcbod.format(name=name)
        function.write(body)
    # This adds the name of the function to a list of stored functions
    # so it can be retrieved easily
    funclist = get_funclist()
    funclist.append("on_" + name)
    store_funclist(funclist)

def remove(name):
    """Does the opposite of store()"""
    try:
        os.remove(f"functions\\on_{name}.py")
    except FileNotFoundError:
        return
    funclist = get_funclist()
    funclist.remove("on_" + name)
    store_funclist(funclist)