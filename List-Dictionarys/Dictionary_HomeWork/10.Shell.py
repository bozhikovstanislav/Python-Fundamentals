import math


def add_shells(text):
    dict_regions = {}
    while text != 'Aggregate':
        info = text.split(' ')
        region = info[0]
        shell = int(info[1])
        if region not in dict_regions:
            dict_regions[region] = []
            dict_regions[region].append(shell)
        else:
            if shell not in dict_regions[region]:
                dict_regions[region].append(shell)
        text = input()
    return dict_regions


def print_regions(all_regions):
    for item in all_regions.items():
        region = item[0]
        list_shells = item[1]
        giant_shell = sum(list_shells) - sum(list_shells) / len(list_shells)
        giant_shell = math.ceil(giant_shell)
        shell_size_str = []
        for sh in list_shells:
            shell_size_str.append(str(sh))
        shells = ', '.join(shell_size_str)
        print(f'{region} -> {shells} ({giant_shell})')


txt = input()
regions = add_shells(txt)
print_regions(regions)