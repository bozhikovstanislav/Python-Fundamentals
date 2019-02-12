import math


def get_average(list_sizes):
    sum_size = sum(list_sizes)
    len_list_sizes = len(list_sizes)
    result = math.ceil(sum_size - (sum_size / len_list_sizes))
    return result


data = input()
shells = {}

while not data == 'Aggregate':
    region = data.split()[0]
    shell_size = int(data.split()[1])

    if not region in shells.keys():
        shells[region] = []
        shells[region].append(shell_size)
    else:
        shells[region].append(shell_size)

    data = input()

for region in shells:
    unique_shells_sizes = sorted(set(shells[region]), key=shells[region].index)
    print(f'{region} -> {", ".join(list(map(str, unique_shells_sizes)))} ({get_average(unique_shells_sizes)})')