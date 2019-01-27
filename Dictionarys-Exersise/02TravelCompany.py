transport_capacity_dict = {}
transport_capacity_list = []

travel_dict = {}
data = input()
while not data == 'ready':
    city_data = data.split(':')[0]
    transport_capacity_list = data.split(':')[1:][0].split(',')
    if city_data not in travel_dict:
        travel_dict[city_data] = {}
        for x in range(len(transport_capacity_list)):
            type_travel = transport_capacity_list[x].split('-')[0]
            capacity_travel = transport_capacity_list[x].split('-')[1]
            travel_dict[city_data][type_travel] = capacity_travel
    elif city_data in travel_dict.keys():
        for x in range(len(transport_capacity_list)):
            type_travel = transport_capacity_list[x].split('-')[0]
            capacity_travel = transport_capacity_list[x].split('-')[1]
            if type_travel in travel_dict[city_data].keys():
                travel_dict[city_data][type_travel] = capacity_travel
    data = input()

print(travel_dict)
