# Normal function
def identity(x):
    return x

print(identity(2))

# Lambda function
x=2
l = lambda x: x
print(l(2))

# Lambda funkcja z dodaniem +1 do argumentu

print((lambda x: x + 1)(2))
add_one = lambda x: x + 1
print(add_one(2))

# zwykład definicja funkcji
def add_one(x):
    return x + 1