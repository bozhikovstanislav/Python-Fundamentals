def sign_number(numberInput):
    if numberInput > 0:
        print('The number ' + f'{number}' + ' is positive.')
    elif numberInput < 0:
        print('The number ' + f'{number}' + ' is negative.')
    else:
        print('The number ' + f'{number}' + ' is zero.')


number = int(input())

sign_number(number)
