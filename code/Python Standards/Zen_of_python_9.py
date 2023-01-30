try:
    print(1/0)
except Exception as e:
    pass


try:
    print(1/0)
except ZeroDivisionError:
    print("Don't divide by zero!")