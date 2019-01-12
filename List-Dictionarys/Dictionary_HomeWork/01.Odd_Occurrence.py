'''
number_list = list(map(str, input().split('|')))
numbers_OK = [number_list[x].split(' ') for x in range(len(number_list) - 1, -1, -1)]
a = [lst[y] for lst in numbers_OK for y in range(0, len(lst)) if lst[y] != '']
print(*a, end=" ")

Input	Output
Java C# PHP PHP JAVA C java	java, c#, c
3 5 5 hi pi HO Hi 5 ho 3 hi pi	5, hi
a a A SQL xx a xx a A a XX c	a, SQL, xx, c

2q  A+.
'''
from typing import Dict, List

words_sentance: List[str] = input().lower().split(' ')
dictionary_word: Dict[int, str] = {}
for i in words_sentance:
    dictionary_word[i] = words_sentance.count(i)

result = []
for k, v in dictionary_word.items():
    if v % 2 != 0:
        result.append(k)

print(", ".join(result))
