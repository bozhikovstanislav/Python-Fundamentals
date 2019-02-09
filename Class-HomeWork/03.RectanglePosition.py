
def is_inside(rect_a, rect_b):
    b_left = rect_a.get_x() >= rect_b.get_x()
    b_top = rect_a.get_y() <= rect_b.get_y()

    b_get_right_ = rect_a.get_x1() <= rect_b.get_x1()
    get_bottum_ = rect_a.get_y1() <= rect_b.get_y1()

    if b_left and b_get_right_ and b_top and get_bottum_:
        return 'Inside'
    return 'Not inside'


class Rectungle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def set_x(self, x):
        if isinstance(x, int):
            return x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        if isinstance(y, int):
            return y

    def get_y(self):
        return self.__y

    def set_width(self, width):
        if isinstance(width, int):
            return width

    def get_width(self):
        return self.__width

    def set_height(self, height):
        if isinstance(height, int):
            return height

    def get_height(self):
        return self.__height

    def get_x1(self):
        h = self.get_x() + abs(self.get_width())
        return h

    def get_y1(self):
        return self.get_y() + self.get_height()


rectungle_one = list(map(int, input().split()))
rectungle_tow = list(map(int, input().split()))

rect_one = Rectungle(rectungle_one[0], rectungle_one[1], rectungle_one[2], rectungle_one[3])
rect_tow = Rectungle(rectungle_tow[0], rectungle_tow[1], rectungle_tow[2], rectungle_tow[3])
print(is_inside(rect_one, rect_tow))
