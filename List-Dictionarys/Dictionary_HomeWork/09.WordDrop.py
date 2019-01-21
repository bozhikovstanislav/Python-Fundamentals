'''
09.Wardrobe
You just bought a new wardrobe.
The weird thing about it is that it came prepackaged with a big box of clothes
(just like those refrigerators, which ship with free beer inside them)!
 So, you’ll need to find something to wear.
4
Blue -> dress,jeans,hat
Gold -> dress,t-shirt,boxers
White -> briefs,tanktop
Blue -> gloves

Blue dress	Blue clothes:
* dress - 1 (found!)
* jeans - 1
* hat - 1
* gloves - 1
Gold clothes:
* dress - 1
* t-shirt - 1
* boxers - 1
White clothes:
* briefs - 1
* tanktop - 1
'''
dress_clotes = []
str


def add_cloth(text):
    wordrop_dic = {}
    count = 0
    while text != count:
        lines_cloth = input()
        if lines_cloth.count(' -> '):
            info = lines_cloth.split(' -> ')
            color = info[0]
            cloth = info[1]
            if color not in wordrop_dic:
                wordrop_dic[color] = []
                wordrop_dic[color].append(cloth)
            else:
                wordrop_dic[color].append(cloth)
            count = count + 1

        else:
            cloth_to_finde = lines_cloth.split(' ')

            for key, v in wordrop_dic.items():
                print(f'{key} clothes:')
                for x, val in times_so_far(count_cloths(v), cloth_to_finde[1]).items():
                    print('* ' + x, '-', val, end="")
                else:
                    print('* ' + x, '-', val)
            break


def search(values, searchFor):
    for k in values:
        if searchFor in k:
            return True
    return False


def read_result(wordrop_dic):
    result = count_cloths(wordrop_dic)
    print(result)


def count_cloths(dictionary_list: list):
    result = [dictionary_list[x].split(',') for x in range(len(dictionary_list))]
    all_joined_list = []
    for i in result:
        for j in i:
            all_joined_list.append(j)
    return all_joined_list


def times_so_far(ls, word_find):
    cloth = {}
    for word in ls:
        if search(ls, word_find):
            cloth[word] = str(cloth.get(word, 0) + 1) + '(found!)'
        else:
            cloth[word] = cloth.get(word, 0) + 1
    return cloth


def cloths(dictionary_list: list):
    result = [dictionary_list[x].split(',') for x in range(len(dictionary_list))]
    all_joined_list = []
    for i in result:
        for j in i:
            all_joined_list.append(j)
    return all_joined_list


txt = input()
colors = add_cloth(txt)
