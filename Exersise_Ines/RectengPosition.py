class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Rectangle:
    def __init__(self, upper_left_point, width, height):
        self.upper_left_point = upper_left_point
        self.width = int(width)
        self.height = int(height)
        self.bottom_right_point = self.get_bottom_right_point()

    def get_bottom_right_point(self):
        x = self.upper_left_point.x + self.width
        y = self.upper_left_point.y + self.height
        point = Point(x, y)
        return point


def is_inside(f_r, s_r):
    left = f_r.upper_left_point.x >= s_r.upper_left_point.x
    right = f_r.bottom_right_point.x <= s_r.bottom_right_point.x
    top = f_r.upper_left_point.y <= s_r.upper_left_point.y
    bottom = f_r.bottom_right_point.y <= s_r.bottom_right_point.y

    if left and right and top and bottom:
        return True
    return False


data_rect_1_list = input().split()
data_rect_2_list = input().split()

point_1 = Point(data_rect_1_list[0], data_rect_1_list[1])
first_rectangle = Rectangle(point_1, data_rect_1_list[2], data_rect_1_list[3])
point_2 = Point(data_rect_2_list[0], data_rect_2_list[1])
second_rectangle = Rectangle(point_2, data_rect_2_list[2], data_rect_2_list[3])

if is_inside(first_rectangle, second_rectangle):
    print("Inside")
else:
    print("Not inside")