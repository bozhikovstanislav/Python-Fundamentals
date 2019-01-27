def make_dict():
    dict_ref = {}
    info = input()
    while info != 'end':
        txt = info.split(' -> ')
        key_to_add = txt[0]
        unknown = txt[1]
        try:
            list_values = list(map(int, unknown.split(', ')))
            if key_to_add not in dict_ref:
                dict_ref[key_to_add] = list_values
            else:
                existing_key_values = dict_ref[key_to_add]
                existing_key_values.extend(list_values)

        except ValueError:
            other_key = unknown
            if other_key in dict_ref:
                dict_ref[key_to_add] = []
                for vals in dict_ref[other_key]:
                    dict_ref[key_to_add].append(vals)
        info = input()
    return dict_ref


def print_dict(final_dict):
    for key, value in final_dict.items():
        val = ', '.join(list(map(str, value)))
        print(f'{key} === {val}')

dict_ref_advanced = make_dict()
print_dict(dict_ref_advanced)