#4

input_data_list = input().split(' ')
print(f'{input_data_list[-1]} ', end='')
print(' '.join(input_data_list[: len(input_data_list)-1]))