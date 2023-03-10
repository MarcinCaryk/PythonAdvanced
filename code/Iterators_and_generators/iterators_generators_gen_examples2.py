# generowanie z generatora
import itertools


def powerset(sequence):
    for size in range(len(sequence) + 1):
        for item in itertools.combinations(sequence, size):
            yield item


for result in powerset('abc'):
    print(result)


def flatten(sequence):
    for item in sequence:
        try:
            yield from flatten(item)
        except TypeError:
            yield item
lst = [1, [2, [3, [4, 5], 6], 7], 8]
print(lst)
print(list(flatten(lst)))