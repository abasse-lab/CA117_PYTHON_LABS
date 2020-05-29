#!/usr/bin/env python3

class Customer(object):
    discount = 0.0

    def __init__(self, name, balance, address1, address2, address3):

        self.name = name
        self.balance = balance
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.discount = self.discount

    def owes(self):
        g = self.balance * self.discount
        return self.balance - g

    def __str__(self):
        return '{:s}'.format(self.name) + '\n' + '{:s}'.format(self.address1) + '\n' + '{:s}'.format(self.address2) + '\n' + '{:s}'.format(self.address3) + '\n' + 'Balance: {:.2f}'.format(self.balance) + '\n' + 'Discount: {:.0f}%'.format(self.discount * 100) + '\n' + 'Amount due: {:.2f}'.format(self.owes())

class ValuedCustomer(Customer):
    discount = 0.1
