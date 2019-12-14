import json

# This first loads the list of functions that are currently stored
with open('functions\\functions.list') as funclist_file:
    funclist = json.load(funclist_file)

# This now imports them all into the file
for funcname in funclist:
    exec(f"from functions.{funcname} import *")