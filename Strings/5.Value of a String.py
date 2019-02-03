sentence = input()
comand = input()
sum = 0
if comand == 'LOWERCASE':
    for x in sentence:
        if x.islower() and x.isalpha():
            sum += ord(x)
    print(f'The total sum is: {sum}')
elif comand == 'UPPERCASE':
    for s in sentence:
        if s.isupper() and s.isalpha():
            sum += ord(s)
    print(f'The total sum is: {sum}')
