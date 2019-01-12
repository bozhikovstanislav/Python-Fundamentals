from typing import List

number_list = list(map(int, input().split(' ')))

list_odd: List[int] = []

list_odd = [print(f'Index {x} -> {number_list[x]}') for x in range(0, len(number_list)) if
            x % 2 != 0 and number_list[x] % 2 != 0]
