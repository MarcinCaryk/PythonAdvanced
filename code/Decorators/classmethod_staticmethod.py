from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # metoda clasy do tworzenia obiektu Person + data urodzenia.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # metoda statyczna określająca czy ossoba jest dorosła.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('ja', 21)
person2 = Person.fromBirthYear('ja', 1996)

print(person1.age)
print(person2.age)
print(Person.isAdult(22))
