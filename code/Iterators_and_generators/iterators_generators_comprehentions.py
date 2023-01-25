# list
squares = [x ** 2 for x in range(10)]
print(squares)

uneven_squares = [x ** 2 for x in range(10) if x % 2]
print(uneven_squares)

import random
print([random.random() for _ in range(10) if random.random() >= 0.5])
print([x for x in [random.random() for _ in range(10)] if x >= 0.5])

# dict
print({x: x ** 2 for x in range(10)})
print({x: x ** 2 for x in range(10) if x % 2})
print({x ** 2: [y for y in range(x)] for x in range(5)})

# set
print([x*y for x in range(3) for y in range(3)])
print({x*y for x in range(3) for y in range(3)})


