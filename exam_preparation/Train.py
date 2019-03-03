def get_name(first_name, last_name):
    return f'{first_name} {last_name}'


def is_valid_card_number(card_number):
    my_sum = sum(list(map(int, card_number)))
    if my_sum % 7 == 0:
        return True
    return False


class ExistingCard:
    def __init__(self, first_name, last_name, card_number):
        self.name = get_name(first_name, last_name)
        self.card_number = card_number


class Destination:
    def __init__(self, location, card_number=None):
        self.location = location
        self.price = self.__get_price()
        self.card_number = card_number

    def __get_price(self):
        my_sum = sum(list(map(ord, self.location))) / 100
        return my_sum

    def set_discount(self):
        self.price = self.price * 0.50


class Passenger:
    def __init__(self, first_name, last_name):
        self.name = get_name(first_name, last_name)
        self.destinations = []
        self.total_sum = 0

    def set_total_sum(self):
        self.total_sum = sum(list(map(lambda dest: dest.price, self.destinations)))


cards = int(input())
existing_cards_list = []

for _ in range(cards):
    first_name, last_name, card_number = input().split()
    existing_card = ExistingCard(first_name, last_name, card_number)
    existing_cards_list.append(existing_card)

data = input()
passengers_list = []

while not data == 'time to leave!':
    _, first_name, last_name, location, card_number = data.split()
    name = get_name(first_name, last_name)
    names_ex_cards_list = list(map(lambda ex_card: ex_card.name, existing_cards_list))
    card_nums_list = list(map(lambda ex_card: ex_card.card_number, existing_cards_list))
    passenger_list = list(filter(lambda p: p.name == name, passengers_list))
    passenger = None

    if passenger_list:
        passenger = passenger_list[0]
    else:
        passenger = Passenger(first_name, last_name)

    if card_number in card_nums_list:

        card = list(filter(lambda ex_card: ex_card.card_number == card_number, existing_cards_list))[0]
        if name == card.name:

            destination = Destination(location, card_number)
            destination.set_discount()


        else:
            print(f'card {card_number} already exists for another passenger!')
            destination = Destination(location)

    else:
        if is_valid_card_number(card_number):
            print(f'issuing card {card_number}')
            existing_card = ExistingCard(first_name, last_name, card_number)
            existing_cards_list.append(existing_card)
            destination = Destination(location, card_number)
            destination.set_discount()

        else:
            print(f'card {card_number} is not valid!')
            destination = Destination(location)

    passenger.destinations.append(destination)
    passengers_list.append(passenger)

    data = input()

unique_passengers_list = list(set(passengers_list))

for passenger in unique_passengers_list:
    passenger.set_total_sum()

ordered_unique_passengers_list = sorted(unique_passengers_list, key=lambda p: -p.total_sum)

for passenger in ordered_unique_passengers_list:
    print(f'{passenger.name}:')
    ordered_destinations = sorted(passenger.destinations, key=lambda d: -d.price)
    for destination in ordered_destinations:
        if destination.card_number:
            print(f'--{destination.location}: {destination.price:.2f}lv (using card {destination.card_number})')
        else:
            print(f'--{destination.location}: {destination.price:.2f}lv')

    print(f'total: {passenger.total_sum:.2f}lv')