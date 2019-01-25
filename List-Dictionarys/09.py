# 09. Insertion Sort Using List*


def insertion_sort_list(old):
    for index in range(1, len(old)):
        cur_val = old[index]
        position = index

        while position > 0 and new[position - 1] > cur_val:
            position = position - 1

        new[position: - index] = [cur_val] # slicing new list


old_list = list(map(int, input().split()))
new = old_list[0:1]
insertion_sort_list(old_list)
print(f"{' '.join(map(str, new))}")