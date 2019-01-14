comands = input()
user_pasword_dic = {}
user_log = []
successful_login = {}
cout_faile_login = 0
while comands != 'end':
    usr_person_pass = list(input().split(' '))
    if not usr_person_pass[0] in user_pasword_dic and usr_person_pass[0] != 'login':
        user_pasword_dic[usr_person_pass[0]] = usr_person_pass[2]
    elif usr_person_pass[0] in user_pasword_dic and usr_person_pass[0] != 'login':
        user_pasword_dic[usr_person_pass[0]] = usr_person_pass[2]

    if usr_person_pass[0] == 'login':
        usr_person_pass = list(input().split(' '))
        if usr_person_pass[0] == 'end':
            break
        elif usr_person_pass[1] in user_pasword_dic.values() and usr_person_pass[0] != 'end':
            user_log.append(f'{usr_person_pass[0]}: logged in successfully')
        else:
            user_log.append(f'{[usr_person_pass[0]]}: login failed')
            cout_faile_login += 1
            successful_login['unsuccessful login attempts:'] = cout_faile_login


print(*[x for x in list(successful_login)], end=" ")
print(*[x for x in list(successful_login.values())])
