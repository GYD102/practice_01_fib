#!/usr/bin/env python3

# In this file, I will try to understand how *args and **kwargs work.

def basic_function(*args, **kwargs):
    s = ("*args prints {}. args prints {} and has type {}. **kwargs prints {}. kwargs prints {} and has type {}.")#.format(
    #)
    print(*args)
    # The below lines will not run. Apart from printing. Note: *args is not an
    # object, args is. Calling *args inside the function just unpacks args the
    # same way it would if making a function call.
    #for i in *args:
    #    print(i)
    #type(*args)
    print(args)
    print(type(args))
    for key, value in kwargs.items():
        print("{} key, {} value".format(key,value))
    # Although print(**kwargs) works when no arguments are passed to kwargs,
    # it fails when arguments are actually passed. Although print(*args) still
    # works.
    #print(**kwargs)
    #type(**kwargs)
    print(kwargs)
    print(type(kwargs))

if __name__ == "__main__":
    # basic_function(1,2,3)
    # a = "hello"
    # print("{} world".format(a))
    basic_function(1,2,3, kw="hello",t="world")
