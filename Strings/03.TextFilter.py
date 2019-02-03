substring_to_check = input().split(' ')
string_text_toCheck = input()

new_string = ""

for x in substring_to_check:
    if x in string_text_toCheck:
        new_string = string_text_toCheck.replace(x, '*' * len(x))
        string_text_toCheck = new_string
print(new_string)
