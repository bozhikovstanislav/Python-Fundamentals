
PI_CONSTANT = 3.141592653589793
a = float(input())
b = float(input())
c = float(input())

n = int(input())

volume_truck = a * b * c
volume_barrel = 0
count_of_barrels = -1

for x in range(0, n):
    r = float(input())
    h = float(input())
    volume_barrel += PI_CONSTANT * r * r * h
    volume_left = volume_truck - volume_barrel
    count_of_barrels += 1
    if volume_left < 0:
        break

if volume_truck < volume_barrel:
    print(f'Truck is full. {count_of_barrels} on board!')
else:
    print(f'All barrels on board. Capacity left - {volume_left:.2f}.')
