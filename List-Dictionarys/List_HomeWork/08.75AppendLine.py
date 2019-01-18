number_list = list(map(str, input().split('|')))
numbers_OK = [number_list[x].split(' ') for x in range(len(number_list) - 1, -1, -1)]
a = []
x: int
for x in range(0, len(numbers_OK)):
    a.append([y for y in numbers_OK[x] if y != ''])
    print(*a[x], end=" ")
