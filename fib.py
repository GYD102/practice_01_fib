#!/usr/bin/env python3
#from functools import wraps
from functools import wraps
import time
from timer_wrapper import time_decorator

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
# After some experimenting, I realized that this could be done using a decorator
# Something to work on in a bit.


#@time_decorator
# I realized that running the above is a bad idea since the timer gets called
# for every recursive call of the function! How do I successfully time only the
# big function call?
def fib_recursive(n):
    if not fib_check_input(n):
        return None
    if n == 0 or n == 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


# Naive iterative fibonacci

# This kind of feels memoized, but it is not. This is because A second function
# call would start calculating l from scratch, whereas a memoized would store
# the values for future function calls.
@time_decorator
def fib_iterative(n):
    if not fib_check_input(n):
        return None
    l = [0,1]
    if n == 0 or n == 1:
        return l[n]
    for i in range(2, n+1):
        l += [l[-2] + l[-1]]
    return l[-1]

def memoize_decorator(funct):
    memo = {}
    @wraps(funct)
    def helper(x):
        if x not in memo:
            memo[x] = funct(x)
        return memo[x]
    return helper


fib_memoized = memoize_decorator(fib_recursive)


if __name__ == "__main__":
    print("Testing shebang.")
    #for i in range(-2,11):
    #    print(fib_recursive(i))

    #for i in range(-2,10000):
    #    print(fib_iterative(i))
    # This iterative test feels way too fast. Let's test separate function calls
    fib_iterative(10000)
    fib_iterative(11500)
    fib_iterative(12000)
    # Interestingly, (likely because of how Python works) making consecutive
    # calls for the same value makes the value faster. Why? Is it because the
    # hardware warms up? Does Python cache certain results? Does the software
    # "warm up"?
    
    #for i in range(-2,11):
    #    print(fib_memoized(i))
        
