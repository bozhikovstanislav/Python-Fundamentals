def upper_part(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(f'{col} ', end='')
        print()


def bodum_part(m):
    for row in range(m, 1, -1):
        for col in range(1, row):
            print(f'{col} ', end='')
        print()


number = int(input())
upper_part(number)
bodum_part(number)
