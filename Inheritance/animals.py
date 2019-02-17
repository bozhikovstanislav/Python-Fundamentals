from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass


animals = []

class Dog(Animal):
    def __init__(self, name, age, number_of_legs ):
        Animal.__init__(self, name, age)
        self.number_of_legs = int(number_of_legs)

    def make_sound(self):
        return "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."

    def __str__(self):
        return f'Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.number_of_legs}'


class Cat(Animal):
    def __init__(self, name, age, intelligence_quotient ):
        Animal.__init__(self, name, age)
        self.intelligence_quotient = int(intelligence_quotient)

    def make_sound(self):
        return "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."

    def __str__(self):
        return f'Cat: {self.name}, Age: {self.age}, IQ: {self.intelligence_quotient}'



class Snake(Animal):
    def __init__(self, name, age, cruelty_coefficient ):
        Animal.__init__(self, name, age)
        self.cruelty_coefficient  = int(cruelty_coefficient )

    def make_sound(self):
        return "I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."

    def __str__(self):
        return f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty_coefficient}'


while True:
    data = input()
    cls = data.split()[0]

    if cls == "I'm":
        break

    elif cls == 'talk':
        name = data.split()[1]
        obj = list(filter(lambda animal: animal.name == name, animals))[0]
        print(obj.make_sound())

    else:
        name = data.split()[1]
        age = data.split()[2]
        third_param = data.split()[3]

        string = f'{cls}("{name}", {age}, {third_param})'
        obj = eval(string)
        animals.append(obj)


dogs = list(filter(lambda animal: isinstance(animal, Dog), animals))
cats = list(filter(lambda animal: isinstance(animal, Cat), animals))
snakes = list(filter(lambda animal: isinstance(animal, Snake), animals))

sorted_animals = dogs + cats + snakes

for animal in sorted_animals:
    print(animal)