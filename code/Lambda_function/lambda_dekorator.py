def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap


@trace
def add_two(x):
    return x + 2

add_two(3)

print((trace(lambda x: x ** 2))(3))


list(map(trace(lambda x: x*2), range(3)))