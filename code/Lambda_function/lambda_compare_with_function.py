import dis

add = lambda x, y: x + y

print(type(add))
dis.dis(add)
print(add)


def addf(x, y): return x + y

print(type(addf))
dis.dis(addf)
print(addf)
