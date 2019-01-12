number_list = list(map(int, input().split(' ')))
number_list_odd = [x for x in number_list if x % 2 != 0]
print(len(number_list_odd))
