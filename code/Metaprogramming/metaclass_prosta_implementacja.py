# Najprostsza implementacja metaklasy, która nic nie robi

class MyMeta(type):
    def __new__(cls, name, bases, namespace):
        return super().__new__(cls, name, bases, namespace)

class MyClass(metaclass=MyMeta):
    x = 3