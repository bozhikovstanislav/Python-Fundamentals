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
x: int
for x in range(0, len(numbers_OK)):
    a.append([y for y in numbers_OK[x] if y != ''])
    print(*a[x], end=" ")
