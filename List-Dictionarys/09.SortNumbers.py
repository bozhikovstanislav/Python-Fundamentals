'''
09.Sort Numbers
Read a list of integers and sort them in ascending order. Print the output as shown in the examples below.

Examples
Input	Output
8 2 7 3	2 <= 3 <= 7 <= 8
2 4 -9	-9 <= 2 <= 4
'''

number_list = list(map(int, input().split(' ')))

sorted_list = sorted(number_list)
result_list = []
for x in range(0, len(sorted_list)):
    if x != len(sorted_list)-1:
        result_list.append(f'{sorted_list[x]} <=')
    else:
        result_list.append(f'{sorted_list[x]}')
print(*result_list)
