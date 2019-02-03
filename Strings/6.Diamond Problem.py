string_diamond = input()
a = [pos for pos, char in enumerate(string_diamond) if char == '<' or char == '>']
caratValueOfTheDiamond = 0
counter = 0
if len(a) != 0:
    for x in range(0, len(a) - 1):
        if string_diamond[a[x]] == '<' and string_diamond[a[x + 1]] == '>':
            d = string_diamond[a[x] + 1:a[x + 1]]
            if d.find('diamond') != -1 or d.find('Diamond') != -1:
                for x in d:
                    if x.isdigit():
                        caratValueOfTheDiamond += int(x)
                print(f'Found {caratValueOfTheDiamond} carat diamond')
                caratValueOfTheDiamond = 0
                counter += 1
    if counter == 0:
        print('Better luck next time')
