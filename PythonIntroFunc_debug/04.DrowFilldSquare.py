# --------
# -\/\/\/-
# -\/\/\/-
# --------


def print_dash_top(n: int):
    for i in range(0, n + 1):
        if i == 0:
            print('-', end="")
        elif i == n:
            print('-', end="")
        else:
            print('--', end="")


def print_middle_part(n: int):
    for i in range(0, n + 1):
        if i == 0:
            print('-', end="")
        elif i == n:
            print('-', end="")
        else:
            print('\\/', end="")


number = int(input())

print_dash_top(number)
print()
for i in range(0,number-2):
    print_middle_part(number)
    print()
print_dash_top(number)
