string_1 = input()

while True:
    command = input()
    if command == 'end':
        break

    command = command.split()
    if command[0] == 'Delete':
        string_1 = string_1[:int(command[1])] + string_1[int(command[2]) + 1:]
    elif command[0] == 'Insert':
        string_1 = string_1[:int(command[1])] + command[2] + string_1[int(command[1]):]
    elif command[0] == 'Right':
        for char in range(int(command[1])):
            string_1 = string_1[-1] + string_1[:-1]
    elif command[0] == 'Left':
        for char in range(int(command[1])):
            string_1 = string_1[1:] + string_1[0]

print(string_1)