number_list = list(map(str, input().split('|')))

a = []

for item in reversed(number_list):
    for number in item:
        if number != " ":
            a.append(number)

print(*a)
