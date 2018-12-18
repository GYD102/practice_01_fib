#!/usr/bin/env python3

# Naive recursive fibonacci

# 1) Validate input.
#    Possible improvements: Do this using raise statement and user-defined
#                           Errors and Exceptions.
#                           Do this using object classes?
#    This was previously done inside the fib_recursive function, but since
#    other versions of the fib function would need to validate the input as
#    well, I decided to make it a separate function.
def fib_check_input(n):
    return type(n) == int and n >= 0

def fib_recursive(n):
    if not fib_check_input(n):
        return None
    if n == 0 or n == 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)
    
def fib_iterative(n):
    if not fib_check_input(n):
        return None

# This /should/(?) be done using a decorator (at least in Python)
def fib_memoize(n):
    return None

if __name__ == "__main__":
    print("Testing shebang.")
    for i in range(-2,11):
        print(fib_recursive(i))

