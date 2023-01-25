# function
def count(start=0, step=1, stop=10):
    n = start
    while n <= stop:
        yield n
        n += step
print(type(count))
print(type(count(10, 2.5, 20)))
for x in count(10, 2.5, 20):
    print(x)

# comprehentions
generator = (x ** 2 for x in range(4))
print(type(generator))
for x in generator:
    print(x)

# Class
class Count(object):
    def __init__(self, start=0, step=1, stop=10):
        self.n = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        n = self.n

        if n > self.stop:
            raise StopIteration()
        self.n += self.step
        return n


for x in Count(10, 2.5, 20):
    print(x)