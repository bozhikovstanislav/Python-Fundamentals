def check_value(list_value):
    val = str(list_value).split(', ')
    for x in val:
        if x.isdigit():
            return True
    return False


data = input()
dic_ref = {}
while not data == 'end':
    key = data.split(' -> ')[0]
    values = data.split(' -> ')[1]
    if check_value(values) and len(values) > 1:
        dic_ref[key] = []
        if key not in dic_ref.keys():
            dic_ref[key] = values
        else:
            dic_ref[key] = dic_ref[key].extend(values)

    data = input()
print(dic_ref)
