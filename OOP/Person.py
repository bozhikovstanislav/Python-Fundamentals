
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val_name):
        self.__name = val_name

    def __str__(self):
        return self.name + "hahah"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age_val):
        self.__age = age_val


class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

