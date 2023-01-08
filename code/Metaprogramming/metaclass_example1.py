class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash(f'{self.name, self.age}')

    def __str__(self):
        return f'Person(name={self.name},age={self.age})'

    def __repr__(self):
        return f'Person(name={self.name},age={self.age})'

