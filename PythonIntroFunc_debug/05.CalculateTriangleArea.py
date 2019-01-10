def calc_triangle_area(base_t: float, height_t: float):
    return 1 / 2 * base_t * height_t


base_tr = input()
height_tr = input()
area_tr = calc_triangle_area(float(base_tr), float(height_tr))

print(f'{area_tr:.12g}')

