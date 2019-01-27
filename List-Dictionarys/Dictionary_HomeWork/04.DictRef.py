'''
04.Dict-Ref
You have been tasked to create a referenced dictionary, or in other words a dictionary, which knows how to reference itself.
You will be given several input lines, in one of the following formats:
{name} = {value}
{name} = {secondName}
The names will always be strings, and the values will always be integers.
In case you are given a name and a value, you must store the given name and its value. If the name already EXISTS, you must CHANGE its value with the given one.
In case you are given a name and a second name, you must store the given name with the same value as the value of the second name. If the given second name DOES NOT exist, you must IGNORE that input.
When you receive the command “end”, you must print all entries with their value, by order of input, in the following format:
{entry} === {value}


Examples
Input	Output
Cash = 500
Johny = 5
Cash = 200
Johnny = 200
Car = 150
Plane = 2000000
end	Cash === 200
Johny === 5
Johnny === 200
Car === 150
Plane === 2000000
Entry1 = 10000
Entry2 = 12345
Entry3 = 10101
Entry4 = Entry1
Entry2 = Entry3
Entry3 = Entry4
end	Entry1 === 10000
Entry2 === 10101
Entry3 === 10000
Entry4 === 10000


'''

comand = None
banck_dic = {}
while True:
    person = list(input().split(','))
    if person[0] == 'end':
        break
    elif person[0] == person[1]:
        banck_dic[person[1]] = banck_dic.get(person[0], 0)
    elif person[0] and person[1].isdigit() in banck_dic:
        banck_dic[person[0]] = int(person[1])
    elif person[1] in banck_dic:
        banck_dic[person[0]] = banck_dic.get(person[1], 0)
    else:
        if person[1].isdigit():
            banck_dic[person[0]] = int(person[1])
for x, v in banck_dic.items():
    print(f'{x} === {v}')
