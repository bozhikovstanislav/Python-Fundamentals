char_dict = {}

while True:
    entry_list = input()
    if entry_list == 'end':
        break

    entry_list = entry_list.split(':')

    char = entry_list[0]
    index = entry_list[1].split('/')
    char_dict[char] = list(map(int, index))

for key, value in sorted(char_dict.items()):
    for v1 in value:
        print(key)

#string = input()

#for char in sorted(set(string), key=string.index):
#    print(char + ":" + ("/".join(map(str, [i for i, ltr in enumerate(string) if ltr == char]))))