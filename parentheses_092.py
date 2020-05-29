#!/usr/bin/env python3

from stack_092 import Stack

lefty = '({['
righty = ')}]'
mapping = {v: k for k, v in zip(lefty, righty)}


def matcher(s):
    stack = Stack()
    for e in s:
        if e in lefty:
            stack.push(e)
        try:
            if e in righty and stack.top() == mapping[e]:
                stack.pop()
        except IndexError:
            return False
    if stack.is_empty():
        return True
    return False
