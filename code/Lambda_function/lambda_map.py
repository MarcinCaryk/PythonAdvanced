# Map
print(list(map(lambda *a: a, range(3))))
print(list(map(lambda *a: a, range(3), 'abc')))
print(list(map(lambda *a: a, range(3), 'abc', range(4, 7))))
print(list(map(lambda *a: a, (1, 2, 3, 4), 'abc')))
print(list(map(lambda x: x**2, range(10))))

# Filter
print(list(filter(lambda x: (x%2 != 0) , [5, 7, 22, 97, 54, 62, 77, 23, 73, 61])))

evens = filter(lambda number: number % 2 == 0, range(10))
odds = filter(lambda number: number % 2 == 1, range(10))
print(f"Even numbers in range from 0 to 9 are: {list(evens)}")
print(f"Odd numbers in range from 0 to 9 are: {list(odds)}")

animals = ["giraffe", "snake", "lion", "squirrel"]
animals_s = filter(lambda animal: animal.startswith('s'), animals)
print(f"Animals that start with letter 's' are: {list(animals_s)}")

# Reduce
from functools import reduce

print(reduce(lambda a, b: a + b, [2, 2]))
print(reduce(lambda a, b: a + b, [2, 2, 2]))
print(reduce(lambda a, b: a + b, range(100)))
print(reduce((lambda x, y: x + y), [5, 8, 10, 20, 50, 100]))

# Dropwhile, takewhile
from itertools import dropwhile,takewhile
print(list(dropwhile(lambda x: x <= 3, [1, 3, 5, 4, 2])))
print(list(takewhile(lambda x: x <= 3, [1, 3, 5, 4, 2])))