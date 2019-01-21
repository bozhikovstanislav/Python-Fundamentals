entrance = list(map(float, input().split()))
index = 0

while True:
    if index + 1 < len(entrance):
        if entrance[index] == entrance[index + 1]:
            entrance[index] = entrance[index] + entrance[index]
            entrance.pop(index + 1)
            index = -1
    else:
        break
    index += 1
print(*entrance)
