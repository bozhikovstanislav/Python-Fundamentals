class Passenger:
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


class Card(Passenger):
    def __init__(self, first_name, last_name, card_number):
        Passenger.__init__(self, first_name, last_name)
        self.card_number = card_number

    @property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, card_number):
        if self.valid_card_number:
            self.__card_number = card_number
        else:
            raise ValueError(f'card {self.card_number} is not valid!')

    @property
    def valid_card_number(self):
        valid = False
        sum_n = 0
        for x in range(len(self.card_number)):
            sum_n += self.card_number[x]
        if sum_n % 7 == 0:
            return True
        return valid


class Ticket(Passenger):
    def __init__(self, first_name, last_name, destination, card):
        Passenger.__init__(self, first_name, last_name)
        self.destination = destination
        self.card = card
        self.ticket_price = self.create_price

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination):
        if isinstance(Destination, destination):
            self.__destination = destination

    @property
    def card(self):
        if self.card.valid_card_number:
            self.ticket_price * 0.5
        return self.__card

    @card.setter
    def card(self, card):
        if isinstance(Card, card):
            self.__card = card

    @property
    def create_price(self):
        suma = 0
        for letter in range(len(self.destination.name_destination)):
            suma += int(self.destination.name_destination[letter])
        value = suma / 100
        return value


class Destination(Ticket):
    def __init__(self, first_name, last_name, name_destination, card):
        Ticket.__init__(self, first_name, last_name, card=card)
        self.name_destination = name_destination

    @property
    def card(self):
        return self.__card

    @card.setter
    def card(self, card):
        if isinstance(Card, card):
            self.__card = card

    @property
    def name_destination(self):
        return self.__name_destination

    @name_destination.setter
    def name_destination(self, name_destination):
        self.__name_destination = name_destination

    def __str__(self):
        passenger = f'{self.card.first_name} {self.card.last_name}:\n'
        destination = f'--{self.name_destination}: {self.ticket_price:.2f}lv'
        return passenger + destination
