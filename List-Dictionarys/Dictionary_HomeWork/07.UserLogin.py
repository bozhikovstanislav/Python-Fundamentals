user_pasword_dic = {}
user_log = {}
successful_login = {}
command = ""

while True:
    usr_person_pass = list(input().split(' '))
    if usr_person_pass[0] == 'login':
        break
    elif not usr_person_pass[0] in user_pasword_dic and usr_person_pass[0] != 'end':
        user_pasword_dic[usr_person_pass[0]] = usr_person_pass[2]
    elif usr_person_pass[0] == 'end':
        break
while True:
    usr_person_pass = list(input().split(' '))
    if usr_person_pass[0] == 'end':
        break
    elif usr_person_pass[2] in user_pasword_dic.values() and usr_person_pass[0] != 'end':
        user_log[usr_person_pass[0]] = 'logged in successfully'
        successful_login[usr_person_pass[0]] = +1
    else:
        user_log[usr_person_pass[0]] = 'login failed'

for x, v in user_log.items():
    print(f'{x}: {v}')
