number_list = list(input().split(' '))

number_list_Copy = number_list.copy()
number_list.pop(len(number_list) - 1)
number_list.insert(0, number_list_Copy[len(number_list_Copy) - 1])
print(*number_list)
