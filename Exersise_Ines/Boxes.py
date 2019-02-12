class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Box:
    def __init__(self, u_l, u_r, b_l, b_r):
        self.upper_left = u_l
        self.upper_right = u_r
        self.bottom_left = b_l
        self.bottom_right = b_r

    def get_width(self):
        return abs(self.upper_right.x - self.upper_left.x)

    def get_height(self):
        return abs(self.bottom_left.y - self.upper_left.y)

    def get_area(self):
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        return 2 * self.get_height() + 2 * self.get_width()

    def __str__(self):
        return f'Box: {self.get_width()}, {self.get_height()}\nPerimeter: {self.get_perimeter()}\nArea: {self.get_area()}'


data = input()
boxes_list = []

while not data == 'end':
    splitted_data = data.split(" | ")
    upper_left_point = Point(splitted_data[0].split(":")[0], splitted_data[0].split(":")[1])
    upper_right_point = Point(splitted_data[1].split(":")[0], splitted_data[1].split(":")[1])
    bottom_left_point = Point(splitted_data[2].split(":")[0], splitted_data[2].split(":")[1])
    bottom_right_point = Point(splitted_data[3].split(":")[0], splitted_data[3].split(":")[1])

    box = Box(upper_left_point, upper_right_point, bottom_left_point, bottom_right_point)
    boxes_list.append(box)

    data = input()

for box in boxes_list:
    print(box)