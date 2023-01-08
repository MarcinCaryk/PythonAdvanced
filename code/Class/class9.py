class Person:
    counter = 0

    def __init__(self, author="Janusz"):
        self.created_by = str(author)
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

person1 = Person("Robot1")
person2 = Person("Robot2")
person3 = Person("Robot3")

print(person1.counter, person2.counter, person3.counter)
person3.counter = 10
print(person1.counter, person2.counter, person3.counter)
type(person1).counter = 5
print(person1.counter, person2.counter, person3.counter)

