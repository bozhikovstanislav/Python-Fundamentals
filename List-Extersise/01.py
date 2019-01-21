number_list = list(map(float, input().split(' ')))
newlist = []
templist = []
count = 0
while True:
    newlist.clear()
    for x in range(len(number_list)):
        if number_list[x] == number_list[x - 1] != number_list[x - 2]:
            newlist.insert(x, number_list[x] + number_list[x - 1])
            newlist.remove(newlist[x - 1])
        else:
            newlist.insert(x, number_list[x])
            count = count + 1
    if count == len(number_list):
        break
    else:
        count = 0
        number_list.clear()
        number_list = newlist[:]
        newlist.clear()

print(*newlist)