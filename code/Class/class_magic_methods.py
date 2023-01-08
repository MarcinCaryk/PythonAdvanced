class Test: pass
t = Test()

class Test1(Test):
    def __repr__(object):
        return 'Testing.Test1'

class Test2(Test):
    def __str__(object):
        return 'Testing.Test2'

print(dir(t))




print(t.__repr__())
print(t.__str__())

print(str(Test1()))
print(repr(Test1()))
print(str(Test2()))
print(repr(Test2()))



import datetime
now = datetime.datetime.now()
print(now.__str__())
print(now.__repr__())
