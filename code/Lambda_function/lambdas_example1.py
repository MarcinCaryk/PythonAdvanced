def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(dispatch_dict('mul', 2, 8))
print(dispatch_dict('unknown', 2, 8))


t = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(t, key=lambda x: x[0]))
print(sorted(t, key=lambda x: x[1]))

print(sorted(range(-5, 6), key=lambda x: x * x))
