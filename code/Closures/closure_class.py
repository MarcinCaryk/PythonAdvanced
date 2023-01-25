class Summer():

    def __init__(self):
        self.data = []

    def __call__(self, val):

        self.data.append(val)
        _sum = sum(self.data)

        return _sum

summer = Summer()

s = summer(1)
print(s)
s = summer(2)
print(s)
s = summer(3)
print(s)
s = summer(4)
print(s)
