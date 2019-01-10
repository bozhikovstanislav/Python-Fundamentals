name = input()
age = int(input())
town = input()
salary = float(input())
salary_to_input='{:.2f}'.format(salary)

if 18 > age > 0:
    age_range = 'teen'
elif 70 > age > 18:
    age_range = 'adult'
else:
    age_range = 'elder'

if 500 > salary > 0:
    salary_range = 'low'
elif 2000 > salary > 500:
    salary_range = 'medium'
else:
    salary_range = 'hight'

extendetinfo = 'Name: ' + f'{name}' + '\n' + 'Age: ' + f'{age}' + '\n' + 'Town: ' + f'{town}' + '\n' + 'Salary: ' + f'${salary_to_input}' + '\n' + 'Age range: ' + f'{age_range}' + '\n' + 'Salary range: ' + f'{salary_range}'

print(extendetinfo)
