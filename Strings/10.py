input_string = input()


def find_all_positions(letter, input_string):
    print(f'{letter}:', end="")
    i = 0
    while i <= len(input_string) - 1:
        if input_string[i] == letter and i == input_string.index(
                letter):  # the first time a letter is met in the string
            print(f'{i}', end="")
            i += 1
            continue
        elif input_string[i] == letter and i != input_string.index(
                letter):  # all other times a letter is met in the string
            print(f'/{i}', end="")
            i += 1
            continue
        elif input_string[i] != letter:  # not the letter we are searching for
            i += 1
        elif i == len(input_string) - 1:  # coming to the end of the string
            print()
            break
    print()


already_printed_letters = ""  # a check in order noto to print any letter more than once
for letter in input_string:
    if letter not in already_printed_letters:
        find_all_positions(letter, input_string)
        already_printed_letters = already_printed_letters + letter

"""
Plamen's elegant solution:

string = input()

for char in sorted(set(string), key=string.index):
    print(char+":"+("/".join(map(str, [i for i, ltr in enumerate(string) if ltr == char]))))
"""