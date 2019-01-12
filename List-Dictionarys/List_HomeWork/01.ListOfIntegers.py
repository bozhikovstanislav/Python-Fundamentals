n_integers = int(input())
number_list = []
sum = 0;
for i in range(0, n_integers):
    number_list.append(input())
    sum += int(number_list[i])
print(sum)
