# funkcja
f = lambda x, y, z: x + y + z
print(f(2, 3, 4))
# Lista lambda
L = [(lambda x: x**2),
    (lambda x: x**3),
    (lambda x: x**4)]
for f in L:
    print(f(2))

# funkcja - porównywanie
lower = (lambda x, y: x if x < y else y)
print(lower('cc', 'bb'))
print(lower(8, 5))

# zagnieżdzenie
action = (lambda x: (lambda y: x + y))
act = action(99)
print(act(2))

# mnożnik
def multip(n):
  return lambda a : a * n

mydoubler = multip(2)
mytripler = multip(3)

print(mydoubler(11))
print(mytripler(11))

# sześcian
cube = lambda x: x*x*x
print(cube(7))