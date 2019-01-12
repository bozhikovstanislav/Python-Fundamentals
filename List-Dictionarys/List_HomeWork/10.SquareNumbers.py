'''
10.Square Numbers
Read a list of integers and extract all square numbers from it and print them in descending order. A square number is an integer which is the square of any integer. For example, 1, 4, 9, 16 are square numbers.
Examples
Input	Output
3 16 4 5 6 8 9	16 9 4
12 1 9 4 16 8 25 49 16	49 25 16 16 9 4 1
'''
from math import sqrt

number_list = list(map(int, (input().split(' '))))

muber_square = []
for x in range(len(number_list)):
    x_ = number_list[x]
    if x_ > 0:
        if sqrt(x_) == int(sqrt(x_)):
            muber_square.append(number_list[x])

print(*reversed(sorted(muber_square)))
