#!/usr/bin/env python3

class Employee(object):
    next_employee_number = 0

    def __init__(self, name, hourly_rate=9.25, hours_worked=0):

        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.employee_number = Employee.next_employee_number
        Employee.next_employee_number += 1

    def add_hours(self, others):
        self.hours_worked += others

    def wages(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return 'Name: {:s}'.format(self.name) + '\n' + 'ID: {:d}'.format(self.employee_number) + '\n' + 'Hours: {:.2f}'.format(self.hours_worked) + '\n' + 'Rate: {:.2f}'.format(self.hourly_rate) + '\n' + 'Wages: {:.2f}'.format(self.wages())
