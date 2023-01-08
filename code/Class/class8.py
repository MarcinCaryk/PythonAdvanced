class Person:
    counter = 0

    def __init__(self, author="Janusz"):
        self.created_by = str(author)
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

person1 = Person("Artur")
print(person1.counter, person1.created_by)
person2 = Person("Joanna")
print(person1.counter, person2.created_by)
person3 = Person("Karol")
print(person1.counter, person3.created_by)

print(person1.counter, person2.counter, person3.counter)
del person2
print(person1.counter, person1.created_by)
del person3
print(person1.counter, person1.created_by)
