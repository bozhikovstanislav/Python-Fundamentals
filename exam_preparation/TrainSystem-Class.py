from abc import abstractmethod,ABC


class Person(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Passenger(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)
        self.cards_list = []
        self.destination_list = []

    @property
    def cards_list(self):
        return self.__cards_list

    @cards_list.setter
    def cards_list(self, cards_list):
        self.__cards_list = cards_list

    def add_card_to_person(self, card):
        self.cards_list.append(card)


class Card(Person):
    def __init__(self, first_name, last_name, card_number):
        Person.__init__(self, first_name, last_name)
        self.card_number = card_number

    @property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, card_number):
        self.__card_number = card_number


class Destination:
    def __init__(self, name_destination, card_passenger, price):
        self.name_destination = name_destination
        self.card_passenger = card_passenger
        self.price = price

    @property
    def name_destination(self):
        return self.__name_destination

    @name_destination.setter
    def name_destination(self, name_destination):
        self.__name_destination = name_destination

    @property
    def card_passenger(self):
        return self.__card_passenger

    @card_passenger.setter
    def card_passenger(self, card_passenger):
        self.__card_passenger = card_passenger

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
