class Employee:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    @property
    def shortcut(self):
        return (''.join([self.__name[0], self.__name[-1], self.__surname[0], self.__surname[-1]])).lower()

    @property
    def email(self):
        return self.shortcut + '@company.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.__name, self.__surname)

    @fullname.setter
    def fullname(self, full_name):
        name, surname = full_name.split(' ')
        self.__name = name
        self.__surname = surname

    @fullname.deleter
    def fullname(self):
        print(f'Delete the name {self.__name} {self.__surname}')
        self.__name = None
        self.__surname = None


e1 = Employee("Marcin", "Caryk")
e1.fullname = "Janusz Bak"

print(e1.fullname)
print(e1.shortcut)
print(e1.email)
