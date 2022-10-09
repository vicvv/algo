from datetime import datetime
import matplotlib.pyplot as plt
from functools import wraps
from functools import reduce
from functools import lru_cache
import numpy


def time_it(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()

        f(*args, **kwargs)

        end_time = datetime.now()
        elapsed = end_time - start_time
        elapsed = elapsed.microseconds

        return elapsed
    return wrapper


@time_it
def fibslow(n):
    if n <= 1:
        return n

    else:
        return fibslow(n-1) + fibslow(n-2)


@time_it
@lru_cache(maxsize=10)
def fibslow_2(n):
    if n <= 1:
        return n

    else:
        return fibslow_2(n-1) + fibslow_2(n-2)


@time_it
def fibfast(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for i in range(1, n+1):
        a, b = b, a + b

    return a


@time_it
def fib_reduce(n):
    return reduce(lambda x, n: [x[1], x[0]+x[1]], range(n), [0, 1])[0]


@time_it
def mm_fib(n):
    return (numpy.matrix([[2, 1], [1, 1]])**(n//2))[0, (n+1) % 2]


@time_it
def fib_ia(n):
    return pow(2 << n, n+1, (4 << 2 * n) - (2 << n)-1) % (2 << n)


if __name__ == '__main__':

    X = range(1, 200)
#    fibslow_times = [fibslow(i) for i in X]
    fibslow_2_times = [fibslow_2(i) for i in X]
    fibfast_times = [fibfast(i) for i in X]
    fib_reduce_times = [fib_reduce(i) for i in X]
    fib_mm_times = [mm_fib(i) for i in X]
    fib_ia_times = [fib_ia(i) for i in X]


    plt.figure()
#   plt.plot(X, fibslow_times, label='Slow Fib')
    plt.plot(X, fibslow_2_times, label='Slow Fib w cache')
    plt.plot(X, fibfast_times, label='Fast Fib')
    plt.plot(X, fib_reduce_times, label='Reduce Fib')
    plt.plot(X, fib_mm_times, label='Numpy Fib')
    plt.plot(X, fib_ia_times, label='Fib ia')
    plt.xlabel('n')
    plt.ylabel('time (microseconds)')
    plt.legend()
    plt.show()