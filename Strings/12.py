user_input = input()
while not user_input == 'end':
    result = None
    for index in range(len(user_input) // 2 + 1):
        if user_input[:index] == user_input[-index:]:
            borders = user_input[:index]
            core = user_input[index:-index]
            if not core == '':
                result = core + borders + core
    if result:
        print(result)
    user_input = input()