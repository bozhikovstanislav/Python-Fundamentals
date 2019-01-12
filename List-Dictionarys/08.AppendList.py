'''
08.Append Lists
Write a program to append several lists of numbers.
Lists are separated by ‘|’.
Values are separated by spaces (‘ ’, one or several)
Order the lists from the last to the first, and their values from left to right.

1 2 3 |4 5 6 |  7  8	7 8 4 5 6 1 2 3
7 | 4  5|1 0| 2 5 |3	3 2 5 1 0 4 5 7
1| 4 5 6 7  |  8 9	    8 9 4 5 6 7 1

'''

number_list = list(map(str, input().split('|')))
numbers_OK = [number_list[x].split(' ') for x in range(len(number_list) - 1, -1, -1)]
a = []
for lst in numbers_OK:
    tmp = [a.append(lst[y]) for y in range(0, len(lst)) if lst[y] != '']
print(*a, end=" ")
