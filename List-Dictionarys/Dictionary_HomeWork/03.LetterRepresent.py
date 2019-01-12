'''
03.Letter Repetition
You will be given a single string, containing random ASCII character.
Your task is to print every character, and how many times it has been used in the string.


'''

words_sentance = list(input())
counts = {}
for num in words_sentance:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
for num in counts.keys():
    print(f'{num} -> {counts[num]}')
