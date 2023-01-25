def make_summer():

    data = []

    def summer(val):

        data.append(val)
        _sum = sum(data)

        return _sum

    return summer

summer = make_summer()
s = summer(1)
print(s)
s = summer(2)
print(s)
s = summer(3)
print(s)
s = summer(4)
print(s)