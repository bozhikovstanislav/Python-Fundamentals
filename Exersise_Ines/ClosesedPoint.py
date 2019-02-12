import math


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class PointsDistance:
    def __init__(self, f_p, s_p, distance):
        self.start_point = f_p
        self.end_point = s_p
        self.distance = distance


def calculate_distance(f_p, s_p):
    side_a = abs(f_p.x - s_p.x)
    side_b = abs(f_p.y - s_p.y)
    result = math.sqrt(side_a ** 2 + side_b ** 2)
    return result


n = int(input())
points_list = []

for _ in range(n):
    data = input()
    x, y = data.split()

    point = Point(x, y)
    points_list.append(point)

distances = []

for index_fp in range(0, len(points_list)):
    for index_sp in range(0, len(points_list)):
        if not index_fp == index_sp:
            distance = calculate_distance(points_list[index_fp], points_list[index_sp])
            distance_points = PointsDistance(points_list[index_fp], points_list[index_sp], distance)
            distances.append(distance_points)

min_distance = sorted(distances, key=lambda distance_points: distance_points.distance)[0]
print(f'{min_distance.distance:.3f}')
print(f'({min_distance.start_point.x}, {min_distance.start_point.y})')
print(f'({min_distance.end_point.x}, {min_distance.end_point.y})')