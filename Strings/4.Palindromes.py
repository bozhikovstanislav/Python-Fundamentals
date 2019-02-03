sentence = input().split()
newSentanc = []
for x in sentence:
    if x[::-1] == x:
        newSentanc.append(x)
sorted_list = sorted(newSentanc, key=lambda s: s.lower())
print(', '.join(sorted_list))
