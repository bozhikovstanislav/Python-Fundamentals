'''
02.Count Real Numbers
Read a list of real numbers and print them in ascending order along with their number of occurrences.

Input	Output		Input	Output		Input	Output
8 2.5 2.5 8 2.5	2.5 -> 3 times
8 -> 2 times		1.5 5 1.5 3	1.5 -> 2 times
3 -> 1 times
5 -> 1 times		-2 0.33 0.33 2	-2 -> 1 times
0.33 -> 2 times
2 -> 1 times
'''
'''

number_list = list(map(float, input().split(' ')))

dictionary_word = {}

for i in number_list:
    dictionary_word[i] = number_list.count(i)

for k, v in sorted(dictionary_word.items()):

    print(f'{round(float(k),2)} -> {v} times')
'''
nums = list(map(float, input().split(' ')))
counts = {}
for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
for num in sorted(counts.keys()):
    print(f'{num} -> {counts[num]} times')
