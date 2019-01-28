#5

list_numbers = [int(x) for x in input().split()]
odd_list = list(filter(lambda x: x%2 == 1, list_numbers))
print(len(odd_list))