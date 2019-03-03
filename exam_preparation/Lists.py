def inc_2(el):
    if el % 2 == 0:
        return el + 2
    return el


def inc_3(el):
    if not el % 2 == 0:
        return el + 3
    return el


data = input()
while not data == 'stop playing':

    nums_list = list(map(int, data.split()))

    if len(nums_list) == len(set(nums_list)):
        nums_list = sorted(list(map(inc_2, nums_list)))
        print(f'Unique list: {",".join(list(map(str, nums_list)))}')
    else:
        nums_list = sorted(list(map(inc_3, nums_list)))
        print(f'Non-unique list: {":".join(list(map(str, nums_list)))}')
    result = sum(nums_list) / len(nums_list)
    print(f'Output: {result:.2f}')
    data = input()