# *args and **kwargs

def my_func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

def my_func2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)


args = [1, 2, 3]
kwargs = {"arg2": 2, "arg1": 1, "arg3": 3}

my_func1(*args)
my_func2(**kwargs)
