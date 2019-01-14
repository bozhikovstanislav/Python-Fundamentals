import math
region_shell = {}


def members(dictArg, keysListArg):
    count_shels = []
    for x in range(0, len(dictArg.values())):
        if dictArg.items() == {}:
            break
        x_ = list(dictArg.values())[x]
        k_ = list(dictArg.keys())[x]
        if x_[0] in keysListArg:
            count_shels.append(x_[1])

    return count_shels


def is_float(input):
    try:
        num = float(input)
    except ValueError:
        return False
    return True


def is_int(input):
    try:
        num = int(input)
    except ValueError:
        return False
    return True


def removeDuplicates(listofElements):
    # Create an empty list to store unique elements
    uniqueList = []

    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)

    # Return the list of unique elements
    return uniqueList


def calculate_averaje(numbers: list):
    sum = 0
    for x in range(0, len(numbers)):
        sum += int(numbers[x])
    average = sum - (sum / len(numbers))
    return average


def input_shell(region_shell: dict):
    counter = 0
    while True:
        usr_person_pass = list(input().split(' '))
        if usr_person_pass[0] == 'Aggregate':
            read_data_(region_shell)
            break
        else:
            region_shell[counter] = usr_person_pass
            counter = counter + 1


def read_data_(reg_shel: dict):
    all_list_v = []
    shel_size = []
    region = []
    val = {k: v for k, v in reg_shel.items()}
    for k, v in val.items():
        all_list_v += v

    for k in all_list_v:
        if is_int(k):
            shel_size.append(k)
        else:
            region.append(k)

    val1 = removeDuplicates(region)
    for regio in val1:
        aver = calculate_averaje(members(reg_shel, regio))
        print(f'{regio} ->', end=' ')
        print(*[', '.join(x for x in members(reg_shel, regio))], end=' ')
        print(f'({math.ceil(aver)})')

input_shell(region_shell)
