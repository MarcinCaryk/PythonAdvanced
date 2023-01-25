# W plikach readline == next()

f1 = open('Always.txt')
print(f1.readline())
print(f1.readline())
print(f1.readline())


f2 = open('Always.txt')
print(f2.__next__())
print(f2.__next__())
print(f2.__next__())


# Skaner plików
f = open('Always.txt')
while True:
    line = f.readline()
    if not line: break
    print(line)