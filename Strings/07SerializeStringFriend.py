text = input()

set_text = sorted(set(text), key=text.index)
list_indexes = []

for letter in set_text:
    print(f"{letter}:", end="")
    for index in range(len(text)):
        if letter == text[index]:
            list_indexes.append(index)
    print("/".join(map(str, list_indexes)))
    list_indexes = []
