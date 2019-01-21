from itertools import groupby

text_input = input()
lower_list = []
upper_list = []
mixted_list = []
count_lower = 0
count_upper = 0
sep = ",;:.!()\"\'\\/[] "
allwords = list([''.join(g) for k, g in groupby(text_input, sep.__contains__) if not k])
for x in range(0, len(allwords)):
    for s in allwords[x]:
        if s.islower() and s.isalpha():
            count_lower += 1
    if count_lower == len(allwords[x]):
        lower_list.append(allwords[x])
    count_lower = 0
for x in range(0, len(allwords)):
    for s in allwords[x]:
        if s.isupper() and s.isalpha():
            count_upper += 1
    if count_upper == len(allwords[x]):
        upper_list.append(allwords[x])
    count_upper = 0
for x in range(0, len(allwords)):
    for s in allwords[x]:
        if s.isupper() and s.isalpha():
            count_upper += 1
        if s.islower() and s.isalpha():
            count_lower += 1
        if not s.isalpha():
            count_lower += 1
        if not s.isalpha():
            count_upper += 1
    if count_lower != 0 and count_upper != 0:
        mixted_list.append(allwords[x])

    count_upper = 0
    count_lower = 0

print('Lower-case:', ', '.join(lower_list))
print('Mixed-case:', ', '.join(mixted_list))
print('Upper-case:', ', '.join(upper_list))
