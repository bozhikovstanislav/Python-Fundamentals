internal = input()
cites_dict = {}
while internal.lower() != 'ready'.lower():
    pair = internal.split(':')
    city_name = pair[0]
    if city_name not in cites_dict:
        cites_dict[city_name] = {}

    for transport in pair[1].split(','):
        transport = transport.split('-')
        transport_type = transport[0]
        transport_capacity = int(transport[1])
        cites_dict[city_name][transport_type] = transport_capacity

    internal = input()

internal = input()
while internal.lower() != 'travel time!'.lower():
    pair = internal.split()
    city_name = pair[0]
    people_count = int(pair[1])
    transport_capacities = 0
    for transport in cites_dict[city_name]:
        transport_capacities += cites_dict[city_name][transport]

    if people_count <= transport_capacities:
        print(f'{city_name} -> all {people_count} accommodated')
    else:
        print(f'{city_name} -> all except {people_count - transport_capacities} accommodated')
    internal = input()