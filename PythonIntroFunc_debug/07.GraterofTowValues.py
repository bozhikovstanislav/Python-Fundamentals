def compare_object(int_a: int, int_b: int)->int:
    if int_a > int_b:
        return int_a
    else:
        return int_b


def compare_object1(object_to_a: str, object_to_b: str) -> str:
    if len(object_to_a) > len(object_to_b):
        return object_to_a
    else:
        return object_to_b


def compare_object2(char_a: chr, char_b: chr) -> chr:
    if char_a > char_b:
        return char_a
    else:
        return char_b


def max_value(type_of_value, object_one, object_tow):
    if type_of_value == 'int':
        return compare_object(int(object_one), int(object_tow))
    elif type_of_value == 'char':
        return compare_object1(object_one, object_tow)
    else:
        return compare_object2(object_one, object_tow)


type_comand = input()
object_a = input()
object_b = input()

print(max_value(type_comand, object_a, object_b))
