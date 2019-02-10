class Animal:
    def __init__(self, name, age, number_l="", iq="", cruelty=""):
        self.__name = self.set_name(name)
        self.__age = self.set_age(age)
        self.__number_l = self.set_number_of_legs(number_l)
        self.__iq = self.set_IQ(iq)
        self.cruelty = self.set_cruelty(cruelty)

    def set_name(self, name):
        if isinstance(name, str):
            return name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if isinstance(age, int):
            return age

    def get_age(self):
        return self.__age

    def set_number_of_legs(self, number_l):
        if isinstance(number_l, int):
            return number_l

    def get_number_of_legs(self):
        return self.__number_l

    def set_IQ(self, iq):
        if isinstance(iq, int):
            return iq

    def get_Iq(self):
        return self.__iq

    def set_cruelty(self, cruelty):
        if isinstance(cruelty, int):
            return cruelty

    def get_cruelty(self):
        return self.cruelty


class Dog(Animal):
    def __init__(self, name, age, number_l):
        super().__init__(name, age, number_l=number_l)

    def prodice_sound(self):
        return f"I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."

    def __str__(self):
        return f'Dog: {self.get_name()}, Age: {self.get_age()}, Number Of Legs: {self.get_number_of_legs()}'


class Cat(Animal):
    def __init__(self, name, age, iq):
        super().__init__(name, age, iq=iq)

    def prodice_sound(self):
        return f"I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."

    def __str__(self):
        return f'Cat: {self.get_name()}, Age: {self.get_age()}, IQ: {self.get_Iq()}'


class Snack(Animal):
    def __init__(self, name, age, cruelty):
        super().__init__(name, age, cruelty=cruelty)

    def prodice_sound(self):
        return f'''I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.'''

    def __str__(self):
        return f'Snake: {self.get_name()}, Age: {self.get_age()}, Cruelty: {self.get_cruelty()}'


dog = []
cat = []
snacke = []
data = input()
while data != "I'm your Huckleberry":
    data_l = data.split(' ')
    if data_l[0] == 'talk':
        for x in range(0, len(dog)):
            if data_l[1] == dog[x].get_name():
                print(dog[x].prodice_sound())
        for x in cat:
            if data_l[1] == x.get_name():
                print(x.prodice_sound())
        for x in snacke:
            if data_l[1] == x.get_name():
                print(x.prodice_sound())
    else:
        animal = data_l[0]
        name_animal = data_l[1]
        age_animal = int(data_l[2])
        ability_animal = int(data_l[3])
        if animal == 'Dog':
            dog.append(Dog(name_animal, age_animal, ability_animal))
        elif animal == 'Cat':
            cat.append(Cat(name_animal, age_animal, ability_animal))
        else:
            snacke.append(Snack(name_animal, age_animal, ability_animal))
    data = input()

for x in dog:
    print(x)
for x in cat:
    print(x)
for x in snacke:
    print(x)
