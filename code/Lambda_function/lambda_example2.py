Y = lambda f: lambda *args: f(Y(f))(*args)

quicksort = Y(lambda f: lambda x: (
        f([item for item in x if item < x[0]])
        + [y for y in x if x[0] == y]
        + f([item for item in x if item > x[0]])
        ) if x else [])


print(quicksort([1, 3, 5, 4, 1, 3, 2]))