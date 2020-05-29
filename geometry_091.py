#!/usr/bin/env python3

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) ** 0.5

class Shape(object):

    def __init__(self, points):
        self.points = points

    def sides(self):
        len_sides = []
        for i in range(1, len(self.points)):
            len_sides.append(self.points[i - 1].distance(self.points[i]))
        len_sides.append(self.points[-1].distance(self.points[0]))
        return len_sides

    def perimeter(self):
        return sum(self.sides())

class Triangle(Shape):

    def area(self):
        a, b, c = self.sides()
        s = (a + b + c) / 2
        A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return A

class Square(Shape):
    def area(self):
        l = self.sides()[0]
        return l ** 2
