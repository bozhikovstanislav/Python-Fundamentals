nums = list(map(int, input().split()))
numbers = []
finished_sorting = False
while not finished_sorting:
    min_value_of_nums = min(nums)
    indeks_of_min_value = nums.index(min_value_of_nums)
    numbers.append(min_value_of_nums)
    nums.pop(indeks_of_min_value)
    if len(nums) == 0:
        del nums
        finished_sorting = True


print(*numbers)