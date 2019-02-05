import math
from itertools import combinations


def get_distance(f_p, s_p):
    side_a = abs(f_p.get_x() - s_p.get_x())
    side_b = abs(f_p.get_y() - s_p.get_y())
    side_c = math.sqrt(side_a ** 2 + side_b ** 2)
    return side_c


def closesed_points(points):
    perm = combinations(list(points), 2)
    dci_value = {}
    for x in list(perm):
        dci_value[(int(x[0].get_x()), int(x[0].get_y())), (int(x[1].get_x()), int(x[1].get_y()))] = get_distance(x[0], x[1])
        minval = min(dci_value.values())
    res = list(filter(lambda x1: dci_value[x1] == minval, dci_value))
    print(f'{minval:.3f}')
    print(f'{res[0][0]}')
    print(res[0][1])


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


n = int(input())
listt_of_points = []
for x in range(0, n):
    first_pont = list(map(float, input().split()))
    first_pont = Point(first_pont[0], first_pont[1])
    listt_of_points.append(first_pont)

closesed_points(listt_of_points)
