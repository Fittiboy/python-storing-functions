from storing_functions import store, remove

def main():
    name = input("What is the name of the function you want to store/remove? ")
    choice = input('Do you want to (s)tore or (r)emove a function? (s/r) ')
    valid_choices = ["s", "r"]
    while choice not in valid_choices:
        choice = input('Please select either "s" for store or "r" for remove: ')
    if choice == "s":
        store(name)
    elif choice == "r":
        remove(name)

if __name__ == "__main__":
    main()
