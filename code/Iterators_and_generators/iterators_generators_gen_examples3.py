# Generator liczb pierwszych
def gen_primes(N):
    primes = set()
    count = 0
    n = 2
    while count < N:
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n
            count = count + 1
        n = n + 1


print(type(gen_primes(100)))
print(gen_primes(10))
print(*gen_primes(10))
print([*gen_primes(10)])

a = [x for x in gen_primes(10)]
print(a)


# Generator liczb fibonacziego
def gen_fibonacci(N):
    c, n = 0, 1
    for i in range(N):
        c, n = n, c + n
        yield c


print(type(gen_fibonacci(10)))
print(*gen_fibonacci(10))