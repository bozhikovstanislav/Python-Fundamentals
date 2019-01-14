user_pasword_dic = {}
user_log = []
successful_login = {}
user_count_log_feiler = {}
user_count_login_suchsesful = {}
command = ""
cout_faile_login = 0
count_sucess_login = 0
successful_login['unsuccessful login attempts:'] = {}
while True:
    usr_person_pass = list(input().split(' '))
    if usr_person_pass[0] == 'login':
        break
    elif not usr_person_pass[0] in user_pasword_dic.values() and usr_person_pass[0] != 'end':
        user_pasword_dic[usr_person_pass[0]] = usr_person_pass[2]
    elif usr_person_pass[0] in user_pasword_dic.values() and usr_person_pass[0] != 'end':
        user_pasword_dic[usr_person_pass[0]] = user_pasword_dic.update(usr_person_pass[2])
while True:
    usr_person_pass = list(input().split(' '))
    if usr_person_pass[0] == 'end':
        break
    elif usr_person_pass[2] in user_pasword_dic.values() and usr_person_pass[0] in user_pasword_dic and usr_person_pass[
        0] != 'end':
        user_log.append(f'{usr_person_pass[0]}: logged in successfully')
    elif not usr_person_pass[0] in user_pasword_dic:
        user_log.append(f'{usr_person_pass[0]}: login failed')
        cout_faile_login += 1
        successful_login['unsuccessful login attempts:'] = cout_faile_login
    elif not usr_person_pass[0] in user_pasword_dic and usr_person_pass[2] in user_pasword_dic.values():
        user_log.append(f'{usr_person_pass[0]}: login failed')
        cout_faile_login += 1
        successful_login['unsuccessful login attempts:'] = cout_faile_login
    else:
        user_log.append(f'{usr_person_pass[0]}: login failed')
        cout_faile_login += 1
        user_count_log_feiler[cout_faile_login] = usr_person_pass[0]
        successful_login['unsuccessful login attempts:'] = cout_faile_login

print("\n".join([user_log[x] for x in range(0, len(user_log))]))
print(*[x for x in list(successful_login)], end=" ")
print(*[x for x in list(successful_login.values())])
