'''
05.Mixed Phones
You will be given several phone entries, in the form of strings in format:
{firstElement} : {secondElement}
The first element is usually the person’s name, and the second one – his phone number.
 The phone number consists ONLY of digits, while the person’s name can consist of any ASCII characters.
Sometimes the phone operator gets distracted by the Minesweeper she plays all day,
 and gives you first the phone, and then the name. e.g. : 0888888888 :
 Pesho. You must store them correctly, even in those cases.
When you receive the command “Over”, you are to print all names you’ve stored with their phones.
 The names must be printed in alphabetical order.
'''
phone_dic = {}
while True:
    person = list(input().split(' : '))
    if person[0] == 'Over':
        break
    if person[1].isdigit():
        phone_dic[person[0]] = person[1]
    elif person[0].isdigit():
        phone_dic[person[1]] = person[0]
for x, v in sorted(phone_dic.items()):
    print(f'{x} -> {v}')
