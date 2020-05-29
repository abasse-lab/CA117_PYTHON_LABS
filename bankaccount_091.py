#!/usr/bin/env python3

class BankAccount(object):

    next_account_number = 16555232
    account_type = 'General'

    def __init__(self, forename, surname, balance):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, others):
        self.balance += others

    def withdraw(self, others):
        current_balance = self.balance - others
        if current_balance < 0:
            print('Insufficient funds available')
        else:
            self.balance -= others

    def __str__(self):
        return 'Name: {:s} {:s}'.format(self.forename, self.surname) + '\n' + 'Account number: {:d}'.format(self.account_number) + '\n' + 'Account type: {:s}'.format(self.account_type) + '\n' + 'Balance: {:.2f}'.format(self.balance)

class CurrentAccount(BankAccount):

    over_draft = -1000.00
    account_type = 'Current'

    def withdraw(self, others):
        current_balance = self.balance - others
        if current_balance < self.over_draft:
            print('Insufficient funds available')
        else:
            self.balance -= others

    def __str__(self):
        return 'Name: {:s} {:s}'.format(self.forename, self.surname) + '\n' + 'Account number: {:d}'.format(self.account_number) + '\n' + 'Account type: {:s}'.format(self.account_type) + '\n' + 'Balance: {:.2f}'.format(self.balance) + '\n' + 'Overdraft: {:.2f}'.format(self.over_draft)

class SavingsAccount(BankAccount):

    interest_rate = 0.01
    account_type = 'Savings'

    def apply_interest(self):
        self.balance *= 1 + SavingsAccount.interest_rate

    def __str__(self):
        return 'Name: {:s} {:s}'.format(self.forename, self.surname) + '\n' + 'Account number: {:d}'.format(self.account_number) + '\n' + 'Account type: {:s}'.format(self.account_type) + '\n' + 'Balance: {:.2f}'.format(self.balance) + '\n' + 'Interest rate: {}'.format(self.interest_rate)
