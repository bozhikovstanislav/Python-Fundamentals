from itertools import groupby

list_numbers = list(map(int, input().split(' ')))
ls = sorted(set(list_numbers))
for x in ls:
    print(f'{x} ->', *[len(list(g[1])) for g in groupby(sorted(list_numbers)) if g[0] == x])
