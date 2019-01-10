def rise_number(base_number: float, number_to_rise: float) -> float:
    return base_number ** number_to_rise


number_one = input()
number_tow = input()

print(rise_number(float(number_one), float(number_tow)))
