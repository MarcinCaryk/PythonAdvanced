# range
r = range(10)
print(r)
print(type(r))
print(list(r))

# map
from math import sqrt
m = map(sqrt, range(9))
print(m)
print(type(m))
print(list(m))

# zip
import random

gracz = ['Gracz1', 'Gracz2', 'Gracz3']
wynik = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

z = zip(gracz, wynik)
print(z)
print(type(z))
print(list(z))