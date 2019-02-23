from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name=None, age=None, gender=None):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def produce_sound(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise Exception('Invalid input!')
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or not age:
            raise Exception('Invalid input!')
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if not gender:
            raise Exception('Invalid input!')
        self.__gender = gender


class Dog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return 'Woof!'


class Frog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return 'Ribbit'


class Cat(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return 'Meow meow'


class Kitten(Cat):
    def __init__(self, name, age, gender):
        Cat.__init__(self, name, age, gender)
        self.gender = 'Female'

    def produce_sound(self):
        return 'Meow'


class Tomcat(Cat):
    def __init__(self, name, age, gender):
        Cat.__init__(self, name, age, gender)
        self.gender = 'Male'

    def produce_sound(self):
        return 'MEOW'


data = None

while True:
    cls = input()
    if cls == 'Beast!':
        break
    data = input().split()
    name = data[0]
    age = int(data[1])
    gender = None

    if len(data) == 3:
        gender = data[2]

    try:
        string = f'{cls}("{name}", age, "{gender}")'
        animal = eval(string)
        print(cls)
        print(f'{animal.name} {animal.age} {animal.gender}')
        print(f'{animal.produce_sound()}')
    except Exception as ex:
        print('Invalid input!')