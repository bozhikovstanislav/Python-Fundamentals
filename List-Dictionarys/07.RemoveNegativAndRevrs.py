'''
07.Remove Negatives and Reverse
Read a list of integers, remove all negative numbers from it and print the remaining items in reversed order.
In case of no items left in the list, print “empty”.
Input	                Output
10 -5 7 9 -33 50	    50 9 7 10
7 -2 -10 1	            1 7
-1 -2 -3	            empty

'''
from typing import List

number_list = list(map(int, input().split(' ')))

remove_neegative: List[int] = [x for x in number_list if x > 0]

remove_neegative.reverse()
if len(remove_neegative) == 0:
    print('empty')
else:
    print(*remove_neegative)
