print((lambda x, y: x + y)(2, 3))


ho_func = lambda x, func: x + func(x)

print(ho_func(2, lambda x: x * x))
print(ho_func(2, lambda x: x + 3))