from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def read_point():
    liniq = input()
    tokens = [float(num) for num in liniq.split(' ')]

    x, y = tokens
    point = Point(x, y)
    return point


def distance_between_points(point1, point2):
    delta_x = point2.x - point1.x
    delta_y = point2.y - point1.y

    distance = sqrt(delta_x ** 2 + delta_y ** 2)
    return distance

point1 = read_point()
point2 = read_point()

distance = distance_between_points(point1, point2)
print(f'{distance:.3f}')
#     def get_x(self):
#         return self.x
#
#     def get_y(self):
#         return self.y
#
#
# def caldistance(point1, point2):
#     delta_x = point2.get_x() - point1.get_x()
#     delta_y = point2.get_y() - point1.get_y()
#
#     distance = sqrt(delta_x**2 + delta_y**2)
#     return distance
#
# p1 = Point(4,3)
# p2 = Point(0,0)
# print(f'{caldistance(p1,p2)}')

