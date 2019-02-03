# It is not considered neccessary that the symbol is met on consequtive lines.
# Might be lines which do not have that symbol, az long as it is met the times needed somewhere below

n = int(input())
str_lines_list = []
for i in range(n):
    str_lines_list.append(input())
# print(str_lines_list)

letter_dict = {}
for str_line in str_lines_list:
    for letter in str_line:
        if letter not in letter_dict:
            letter_dict[letter] = []

# print(letter_dict)

for letter, letter_list in letter_dict.items():
    l = 1
    for str_line in str_lines_list:
        wanted = letter * l
        if wanted in str_line:
            letter_dict[letter].append(wanted)
            l += 2

wanted_letter = ""
last_best = 0
for letter in letter_dict:
    if len(letter_dict[letter]) > last_best:
        last_best = len(letter_dict[letter])
        wanted_letter = letter

for line in letter_dict[wanted_letter]:
    print(line)