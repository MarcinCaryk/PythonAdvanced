def go(word):
    yield word
    yield 2 * word
    yield 4 * word


a = go('Hello')
print(next(a))
print(next(a))
print(next(a))


# generator
def gensq(N):
    for i in range(N):
        yield i ** 2

for x in gensq(10): print(x, end=' : ')

# comprehansion
print('\n')
for x in [n ** 2 for n in range(10)]: print(x, end=' : ')

# iterator map
print('\n')
for x in map((lambda n: n ** 2), range(10)): print(x, end=' : ')