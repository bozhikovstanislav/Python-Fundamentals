list_numbers = list(map(int, input().split(' ')))

number = int(input())

flag = True
for x in list_numbers:
    if x == number:
        flag = False
if flag:
    print("no")
else:
    print("yes")
