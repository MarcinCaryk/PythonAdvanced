multipliers = []
for x in range(1, 4):
    multipliers.append(lambda y: x * y)

m1, m2, m3 = multipliers
a = 10

print(m1(a))
print(m2(a))
print(m3(a))


def multiplier(x):
    def multiply(y):
        return x * y
    return multiply


multipliers = []
for x in range(1, 4):
    multipliers.append(multiplier(x))

m1, m2, m3 = multipliers

print(m1(a))
print(m2(a))
print(m3(a))