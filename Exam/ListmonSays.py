def unique_values(g):
    s = set()
    for x in g:
        if x in s:
            return False
        s.add(x)
    return True


def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


entrance = list(map(int, input().split()))

data = input()
count = 0
while not data == "exhausted":
    input_data = data.split()
    if input_data[0] == 'set':
        count += 1
        if unique_values(entrance):
            print("It is a set")
        else:
            unique_list = unique(entrance)
            print(unique_list)
    elif input_data[0] == 'filter':
        count += 1
        if input_data[1] == 'odd':
            only_odd = [num for num in entrance if num % 2 == 1]
            print(only_odd)
        elif input_data[1] == 'even':
            only_even = [num for num in entrance if num % 2 != 1]
            print(only_even)
    elif input_data[0] == 'multiply':
        count += 1
        number_to_multiply = int(input_data[1])
        my_new_list = [i * number_to_multiply for i in entrance]
        print(my_new_list)

    elif input_data[0] == 'divide':
        count += 1
        number_to_multiply = int(input_data[1])
        if number_to_multiply == 0:
            print('ZeroDivisionError caught')
        else:
            my_new_list = [i / number_to_multiply for i in entrance]
            print(my_new_list)
    elif input_data[0] == 'slice':
        count += 1
        n_input = int(input_data[1])
        m_input = int(input_data[2]) + 1
        sliced_list = entrance[n_input: m_input]
        if len(entrance) < m_input:
            print('IndexError caught')
        else:
            print(sliced_list)
    elif input_data[0] == 'sort':
        count += 1
        sorted_list = sorted(entrance, reverse=False)
        print(sorted_list)
    elif input_data[0] == 'reverse':
        count += 1
        sorted_rev = ls = entrance[::-1]
        print(sorted_rev)
    data = input()
print(f'I beat It for {count} rounds!')
