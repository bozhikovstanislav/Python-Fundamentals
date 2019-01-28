2
list_ = list(map(float, input().split()))

dict_ = {}

for num in list_:
   dict_[num] = list_.count(num)

for item in sorted(dict_.items()):
   print(f'{item[0]} -> {item[1]} times')