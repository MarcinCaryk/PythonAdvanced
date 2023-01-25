def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

m1 = multiplier(1)
m2 = multiplier(2)
m3 = multiplier(3)

a = 10

print(m1(a))
print(m2(a))
print(m3(a))