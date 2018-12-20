#!/usr/bin/env python3

from functools import wraps
import time

def time_decorator(funct):
    @wraps(funct)
    def mod(*args):
        t1 = time.time()
        ret = funct(args[0])
        print("It took {} seconds to run function {} with args {}".format(
            time.time()-t1,
            funct.__name__,
            args)
        )
        return ret
    return mod

@time_decorator
def test_funct():
    time.sleep(3)

if __name__ == "__main__":
    test_funct()
