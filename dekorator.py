from functools import wraps
import time

def timeit(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        """to jest z wrappera"""
        t = time.time()
        r = func(*args, **kwargs)
        print(time.time() - t, "s")
        return r
    # wrapper.__name__ = func.__name__

    return wrapper


@timeit
def foo(n):
    """Opis funkcji foo"""
    return sum([x**10 for x in range(n)])


def foo2(n):
    """Opis funkcji foo2"""
    return sum([x**20 for x in range(n)])

# foo = timeit(foo)

# print(foo(1000))
# help(foo)
help(foo)
