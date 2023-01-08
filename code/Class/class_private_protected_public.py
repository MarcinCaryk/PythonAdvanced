class TestTemplate(object):
    def __init__(self, tag='', functionality=None, status=False):
        self.__status = status
        self._tag = tag
        self.functionality = functionality

test = TestTemplate(tag="SmokeTest", functionality="AnyTest", status=True)

print('{:#^15}'.format("Public"))
print(test.functionality)
test.functionality = "ThisTest"
print(test.functionality)

print('{:#^15}'.format("Private"))
print(test._tag)
test._tag = "RegTest"
print(test._tag)

print('{:#^15}'.format("Protected"))
print(test.__status)
print(test._TestTemplate__status)
