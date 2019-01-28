transport_capacity_list = []
travel_dict = {}
data = input()
while data.lower() != 'ready'.lower():
    city_data = data.split(':')[0]
    transport_capacity_list = data.split(':')[1:][0].split(',')
    if city_data not in travel_dict:
        travel_dict[city_data] = {}
        for x in range(len(transport_capacity_list)):
            type_travel = transport_capacity_list[x].split('-')[0]
            capacity_travel = transport_capacity_list[x].split('-')[1]
            travel_dict[city_data][type_travel] = int(capacity_travel)
    elif city_data in travel_dict.keys():
        for x in range(len(transport_capacity_list)):
            type_travel = transport_capacity_list[x].split('-')[0]
            capacity_travel = transport_capacity_list[x].split('-')[1]
            if type_travel in travel_dict[city_data].keys():
                travel_dict[city_data][type_travel] = int(capacity_travel)
    data = input()

data_travel = input()

while data_travel.lower() != 'travel time!'.lower():
    group_to_travel = data_travel.split(' ')
    city_to_go = group_to_travel[0]
    number_of_people = int(group_to_travel[1])
    seats = 0
    for x, v in travel_dict.items():
        if city_to_go in x:
            for xw, f in v.items():
                seats += int(f)
    if number_of_people <= seats:
        print(f'{city_to_go} -> all {number_of_people} accommodated')
    elif number_of_people > seats:
        print(f'{city_to_go} -> all except {number_of_people - seats} accommodated')
    data_travel = input()
