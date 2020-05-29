#!/usr/bin/env python3

class BankAccount(object):

    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0):
        self.forename = forename
        self.surname = surname
        self.balance = balance

        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, others):
        self.balance += others
        BankAccount.total_lodgements += 1

    def apply_interest(self):
        self.balance *= 1 + BankAccount.interest_rate

    def __iadd__(self, others):
        self.lodge(others)
        return self

    def __str__(self):
        return 'Name: {:s} {:s}'.format(self.forename, self.surname) + '\n' + 'Account number: {:d}'.format(self.account_number) + '\n' + 'Balance: {:.2f}'.format(self.balance)
    
    def withdraw(self, others):
        current_balance = self.balance - others
        if current_balance < self.over_draft:
            print('Insufficient funds available')
        else:
            self.balance -= others

    def withdraw(self, others):
        current_balance = self.balance - others
        if current_balance < 0:
            print('Insufficient funds available')
        else:
            self.balance -= others