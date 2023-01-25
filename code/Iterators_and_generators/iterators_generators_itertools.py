# itertools - accumulate
from operator import add
from itertools import accumulate
numbers = [5, 8, 10, 20, 50, 100]
print(list(accumulate(numbers, add)))

# itertools - chain
from itertools import chain
a = range(3)
b = range(5)
print(list(chain(a, b)))

# itertools - combination
from itertools import combinations
print(list(combinations(range(3), 2)))

# itertool - permutation
from itertools import permutations
print(list(permutations(range(3), 2)))

# itertool - compress
from itertools import compress
print(list(compress(range(1000), [0, 1, 1, 1, 0, 1, 0, 0, 1])))

# itertools - dropwhile, takewhile
from itertools import dropwhile,takewhile
print(list(dropwhile(lambda x: x <= 3, [1, 3, 5, 4, 2])))
print(list(takewhile(lambda x: x <= 3, [1, 3, 5, 4, 2])))

# itertools - islice
from itertools import islice

lines = ["line1", "line2", "line3", "line4", "line5",
         "line6", "line7", "line8", "line9", "line10"]

first_five_lines = islice(lines, 1, 5, 2)
for line in first_five_lines:
    print(line)

# itertools - pairwise
from itertools import pairwise

for pair in pairwise('ABCDEFGHI'):
    print(pair[0], pair[1])