import math


def get_distance(f_p, s_p):
    side_a = abs(f_p.get_x() - s_p.get_x())
    side_b = abs(f_p.get_y() - s_p.get_y())
    side_c = math.sqrt(side_a ** 2 + side_b ** 2)
    return side_c


def calculate_perimeter(width, height):
    return 2 * width + 2 * height


def calculate_area(width, height):
    return width * height


class Point:
    def __init__(self, x, y):
        self.__x = self.set_x(x)
        self.__y = self.set_y(y)

    def get_y(self):
        return self.__y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if isinstance(x, int):
            return x


    def set_y(self, y):
        if isinstance(y, int):
            return y



class Boxes:
    def __init__(self, up_left_p, up_right_p, bot_left_p, bot_right_p):
        self.__up_left_p = self.set_up_left_p(up_left_p)
        self.__up_right_p = self.set_up_right_p(up_right_p)
        self.__bot_left_p = self.set_bot_left_p(bot_left_p)
        self.__bot_right_p = bot_right_p

    def set_up_left_p(self, up_left_p):
        if isinstance(up_left_p, Point):
            return up_left_p

    def get_up_left_p(self):
        return self.__up_left_p

    def set_up_right_p(self, up_right_p):
        if isinstance(up_right_p, Point):
            return up_right_p

    def get_up_right_p(self):
        return self.__up_right_p

    def set_bot_left_p(self, bot_left_p):
        if isinstance(bot_left_p, Point):
            return bot_left_p

    def get_bot_left_p(self):
        return self.__bot_left_p

    def set_bot_right_p(self, bot_right_p):
        if isinstance(self, bot_right_p):
            return bot_right_p

    def get_bot_right_p(self):
        return self.__bot_right_p

    def get_width(self):
        return get_distance(self.get_up_left_p(), self.get_up_right_p())

    def get_height(self):
        return get_distance(self.get_up_left_p(), self.get_bot_left_p())

    def __str__(self):
        a = f'Box: {int(self.get_width())}, {int(self.get_height())}\n'
        b = f'Perimeter: {int(calculate_perimeter(self.get_width(), self.get_height()))}\n'
        c = f'Area: {int(calculate_area(self.get_width(), self.get_height()))}'
        return a + b + c


data = input()
boxes_lst = []
while data != "end":
    data_lst = data.split('|')
    x1y1 = data_lst[0].split(':')
    x1 = int(x1y1[0])
    y1 = int(x1y1[1])
    up_left_p_i = Point(x1, y1)

    x2y2 = data_lst[1].split(':')
    x2 = int(x2y2[0])
    y2 = int(x2y2[1])
    up_right_p_i = Point(x2, y2)

    x3y3 = data_lst[2].split(':')
    x3 = int(x3y3[0])
    y3 = int(x3y3[1])
    bot_left_p_i = Point(x3, y3)

    x4y4 = data_lst[3].split(':')
    x4 = int(x4y4[0])
    y4 = int(x4y4[1])
    bot_right_p_i = Point(x4, y4)

    box = Boxes(up_left_p_i, up_right_p_i, bot_left_p_i, bot_right_p_i)
    boxes_lst.append(box)
    data = input()

for x in boxes_lst:
    print(x)
