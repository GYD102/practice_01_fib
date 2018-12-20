#!/usr/bin/env python3

# Practicing using decorator functions
from functools import wraps


def decorator_0(funct):
    @wraps(funct)
    # Note, you don't need to pass funct to the def of the inner function
    def wrap():
        # Here is some additional functionality
        print("This is decorator_1 reporting!")
        # Here is where we keep the functionality of the old function
        return funct()
    # We then return the new ("mutated") function
    return wrap

# The @ line is the equivalent of: base = decorator_1(base) after base is
# created. In other words, base() is overwritten by it's "mutated" form.
@decorator_0
def base_0():
    print("This is the base function!")


def decorator_1(funct):
    @wraps(funct)
    def wrap(*args):
        if len(args) != 1:
            print("Warning! You entered too many arguments, using first argument only!")
        if not type(args[0]) == int:
            print("Error! You passed a non-integer!")
            return None
        return funct(args[0])
    return wrap

@decorator_1
def base_1(n):
    print(n+1)
    return n+1

    
if __name__ == "__main__":
    base_0()
    base_1(2)
    base_1(1.1)
    base_1(6,4,3)
