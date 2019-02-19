# 1 2  3   4 5 6 1 1 2   2 1 4 7 7 8 8      5 5 5 5

from collections import Counter

data = input()
sum_odd_element = 0
sorted_list_od = []
non_uniqe_list = []


def unique_values(g):
    s = set()
    for x in g:
        if x in s:
            return False
        s.add(x)
    return True


def print_non_unique():
    for n in list_numbers:
        if n % 2 != 0:
            n += 3
        non_uniqe_list.append(n)

    if len(non_uniqe_list) > 0:
        out_no_unique = sum(non_uniqe_list) / len(non_uniqe_list)
        print('Non-unique list: ' + ":".join(map(str, sorted(non_uniqe_list))))
        print(f'Output: {out_no_unique:.2f}')
        non_uniqe_list.clear()


def print_unique():

    for x in list_numbers:
        if x % 2 == 0:
            x += 2
        sorted_list_od.append(x)
    if len(sorted_list_od) > 0:
        out_put = sum(sorted_list_od) / len(sorted_list_od)
        print('Unique list: ' + ",".join(map(str, sorted(sorted_list_od))))
        print(f'Output: {out_put:.2f}')
        sorted_list_od.clear()


while not data == "stop playing":
    list_numbers = list(map(int, data.split()))
    if unique_values(list_numbers):
        print_unique()
    else:
        print_non_unique()

    data = input()
