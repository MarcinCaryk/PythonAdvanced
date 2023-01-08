class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass

    def swim(self):
        pass

    def run(self):
        pass

    def fly(self):
        pass

    def crawl(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animals = [
    Lion('lion'),
    Mouse('mouse'),
    Snake('snake')
]
animal_sound(animals)
