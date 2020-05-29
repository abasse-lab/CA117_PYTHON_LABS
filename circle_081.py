#!/usr/bin/env python3

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, others):
        return Point((self.x + others.x) / 2, (self.y + others.y) / 2)

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)


class Circle(object):
    def __init__(self, p, r=0):
        self.x = p.x
        self.y = p.y
        self.r = r

    def midpoint(self, others):
        return Point((self.x + others.x) / 2, (self.y + others.y) / 2)

    def __add__(self, others):
        a = self.midpoint(others)
        r = int(self.r) + int(others.r)
        return Circle(a, r)

    def __str__(self):
        return 'Centre: ({:.1f}, {:.1f})'.format(self.x, self.y) + '\n' + 'Radius: {}'.format(self.r)
