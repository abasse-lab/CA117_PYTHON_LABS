#!/usr/bin/env python3

class Employee(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def wages(self):
        return 0.00

    def __str__(self):
        return 'Name: {:s}'.format(self.name) + '\n' + 'Number: {:d}'.format(self.number) + '\n' + 'Wages: {:.2f}'.format(self.wages())

class Manager(Employee):
    def __init__(self, name, number, wage):
        super().__init__(name, number)
        self.wage = wage

    def wages(self):
        return self.wage / 52

class AssemblyWorker(Employee):
    def __init__(self, name, number, hourly_rate, hours):
        super().__init__(name, number)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def wages(self):
        return self.hourly_rate * self.hours
