from __future__ import print_function

person_info = {}


def print_double_line():
    print('====================')


def members(dictArg, keysListArg):
    count = 0
    for x in range(0, len(dictArg.values())):
        if dictArg.items() == {}:
            break
        x_ = list(dictArg.values())[x]
        k_ = list(dictArg.keys())[x]
        if x_[0] in keysListArg[0]:
            count = k_
    return count


def count_names(info_dic: dict):
    count = 0
    value = []
    for k, v in info_dic.items():
        value = info_dic.get(k)


def is_float(input):
    try:
        num = float(input)
    except ValueError:
        return False
    return True


def is_positive(number: str):
    if number.index(number, 0) == '-':
        return False
    return True


def is_int(input):
    try:
        num = int(input)
    except ValueError:
        return False
    return True


def input_personal(personal_info: dict):
    counter = 0
    while True:
        usr_person_pass = list(input().split(' -> '))
        if usr_person_pass[0] == 'filter base':
            filter_base_p_info(personal_info)
            break
        else:
            if usr_person_pass == '':
                usr_person_pass = None
            person_info[counter] = usr_person_pass
            counter = counter + 1


def filter_base_p_info(data_base_info: dict):
    while True:
        comand = input()
        val = {k: v for k, v in data_base_info.items()}
        if comand == 'Age':
            for k, v in val.items():
                float(v[1])
                if float(v[1]) % 1 == 0:
                    print(f'Name: {v[0]}')
                    print(f'Age: {v[1]}')
                    print_double_line()
        elif comand == 'Salary':
            for pv, pk in val.items():
                if is_float(pk[1]) and not is_int(pk[1]):
                    print(f'Name: {pk[0]}')
                    print(f'Salary: {pk[1]}')
                    print_double_line()
        elif comand == 'Position':
            for pv, pk in val.items():
                if not is_int(pk[1]) and not is_float(pk[1]):
                    print(f'Name: {pk[0]}')
                    print(f'Position: {pk[1]}')
                    print_double_line()
        else:
            break
        break


input_personal(person_info)
