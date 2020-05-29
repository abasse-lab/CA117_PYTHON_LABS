2#!/usr/bin/env python3

import sys
import calendar

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
a = ["Monday's child is fair of face.", "Tuesday's child is full of grace.", "Wednesday's child is full of woe.", "Thursday's child has far to go.", "Friday's child is loving and giving.", "Saturday's child works hard for a living.", "Sunday's child is fair and wise and good in every way."]

day = int(sys.argv[3])
month = int(sys.argv[2])
year = int(sys.argv[1])

if calendar.weekday(day, month, year) == 0:
    print("You were born on a Monday and", a[0])
elif calendar.weekday(day, month, year) == 1:
    print("You were born on a Tuesday and", a[1])
elif calendar.weekday(day, month, year) == 2:
    print("You were born on a Wednesday and", a[2])
elif calendar.weekday(day, month, year) == 3:
    print("You were born on a Thursday and", a[3])
elif calendar.weekday(day, month, year) == 4:
    print("You were born on a Friday and", a[4])
elif calendar.weekday(day, month, year) == 5:
    print("You were born on a Saturday and", a[5])
elif calendar.weekday(day, month, year) == 6:
    print("You were born on a Sunday and", a[6])
   
