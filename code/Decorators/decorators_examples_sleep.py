import functools
import time

def slow_function(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_function
def countdown(from_number):
    if from_number < 1:
        print("Koniec")
    else:
        print(from_number)
        countdown(from_number - 1)


countdown(10)