#!/usr/bin/env python3

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def distance(self, p):
        return ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) ** 0.5

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class Segment(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        return '({}, {})'.format((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)

    def length(self):
        return self.p1.distance(self.p2)

class Circle(object):
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def overlaps(self, c2):
        return self.radius + c2.radius > self.centre.distance(c2.centre)
