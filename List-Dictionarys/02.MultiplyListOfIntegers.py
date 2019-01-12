number_list = list(map(int, input().split(' ')))

number_p = int(input())

multiplyList = [number_p * x for x in number_list]

print(*multiplyList)