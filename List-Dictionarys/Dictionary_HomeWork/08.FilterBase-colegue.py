text = input()
Age = {}
Salary = {}
Position = {}

while text != 'filter base':
    user_data = text.split(' -> ')
    name = user_data[0]
    age_num = 0
    salary_num = 0
    position_txt = ''
    try:
        float(user_data[1])
        if float(user_data[1]) % 1 == 0:
            age_num = int(float(user_data[1]))
            Age[name] = age_num
        else:
            salary_num = float(user_data[1])
            Salary[name] = salary_num
    except:
        position_txt = user_data[1]
        Position[name] = position_txt
    text = input()

if text == 'filter base':
    controller = input()

if controller == 'Salary':
    for key, value in Salary.items():
        print(f'Name: {key}')
        print(f'{controller}: {value}')
        print('====================')
elif controller == 'Age':
    for key, value in Age.items():
        print(f'Name: {key}')
        print(f'{controller}: {value}')
        print('====================')
elif controller == 'Position':
    for key, value in Position.items():
        print(f'Name: {key}')
        print(f'{controller}: {value}')
        print('====================')