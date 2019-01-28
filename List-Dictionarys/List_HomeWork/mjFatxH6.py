#7 

list_data = list(map(int, input().split()))

positive_list = [x for x in list_data if x > 0]

if positive_list:
   print(*reversed(positive_list))
else:
   print('empty')