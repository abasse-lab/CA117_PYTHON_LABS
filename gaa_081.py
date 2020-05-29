#!/usr/bin/env python3
        return Score(self.goals * others, self.points * others)

def score2points(scoreclass):
    return scoreclass.goals * 3 + scoreclass.points

class Score(object):
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __eq__(self, others):
        return score2points(self) == score2points(others)

    def __gt__(self, others):
        return score2points(self) > score2points(others)

    def __lt__(self, others):
        return score2points(self) < score2points(others)

    def __ge__(self, others):
        return score2points(self) >= score2points(others)

    def __le__(self, others):
        return score2points(self) <= score2points(others)

    def __add__(self, others):
        tg = self.goals + others.goals
        tp = self.points + others.points
        return Score(tg, tp)

    def __sub__(self, others):
        tg = self.goals - others.goals
        tp = self.points - others.points
        return Score(tg, tp)

    def __iadd__(self, others):
        z = self + others
        self.goals, self.points = z.goals, z.points
        return self

    def __isub__(self, others):
        z = self - others
        self.goals, self.points = z.goals, z.points
        return self

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(self.goals, self.points)
