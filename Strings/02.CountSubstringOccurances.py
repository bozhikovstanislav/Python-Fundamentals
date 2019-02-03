string_text_toCheck = input().lower()
substring_to_check = input()


def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub.lower(), start) + 1
        if start > 0:
            count += 1
        else:
            return count


print(occurrences(string_text_toCheck, substring_to_check))
