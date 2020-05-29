#!/usr/bin/env python3

class Score(object):
    def __init__(self, goal=0, points=0):
        self.goal = goal
        self.points = points

    def greater_than(self, score2):
        if (self.points + self.goal * 3) > (score2.points + score2.goal * 3):
            return True
        else:
            return False

    def less_than(self, score2):
        if (self.points + self.goal * 3) < (score2.points + score2.goal * 3):
            return True
        else:
            return False

    def equal_to(self, score2):
        if (self.points + self.goal * 3) == (score2.points + score2.goal * 3):
            return True
        else:
            return False
