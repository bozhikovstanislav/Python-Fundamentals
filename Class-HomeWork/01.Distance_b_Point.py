import math


def get_distance(f_p, s_p):
    side_a = abs(f_p.get_x() - s_p.get_x())
    side_b = abs(f_p.get_y() - s_p.get_y())
    side_c = math.sqrt(side_a ** 2 + side_b ** 2)
    return side_c


class Point:
    def __init__(self, x, y):
        self.__x = self.set_x(x)
        self.__y = self.set_y(y)

    def get_y(self):
        return self.__y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if isinstance(x, float):
            return x
        return Exception

    def set_y(self, y):
        if isinstance(y, float):
            return y
        return Exception


first_pont = list(map(float, input().split()))
first_pont = Point(first_pont[0], first_pont[1])
second_point = list(map(float, input().split()))
second_point = Point(second_point[0], second_point[1])
distance = get_distance(first_pont, second_point)

print(f'{distance:.3f}')
