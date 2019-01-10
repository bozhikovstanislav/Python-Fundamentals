def sum_oddDigit(number: str):
    sum = 0
    if number[0] == '-':
        for i in range(1, len(number)):
            if int(number[i]) % 2 != 0:
                sum += int(number[i])
    else:
        for i in range(0, len(number)):
            if int(number[i]) % 2 != 0:
                sum += int(number[i])
    return sum


def sum_even_digit(number: str):
    sum = 0
    if number[0] == '-':
        for i in range(1, len(number)):
            if int(number[i]) % 2 == 0:
                sum += int(number[i])
    else:
        for i in range(0, len(number)):
            if int(number[i]) % 2 == 0:
                sum += int(number[i])
    return sum


def multiply_sum_odd_even(number: str):
    even_sum = sum_even_digit(number)
    odd_sum = sum_oddDigit(number)
    return even_sum * odd_sum


number = input()

print(multiply_sum_odd_even(number))
