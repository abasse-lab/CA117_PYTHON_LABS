#!/usr/bin/env python3

class Contact(object):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return '{} {} {}'.format(self.name, self.phone, self.email)

class ContactList(object):
    def __init__(self, d={}):
        self.d = d

    def add_contact(self, other):
        self.d[other.name] = other

    def del_contact(self, name):
        if name in self.d:
            del self.d[name]

    def get_contact(self, name):
        if name in self.d:
            return str(self.d[name])
        else:
            return None

    def __str__(self):
        sorted_list = [str(self.d[x]) for x in sorted(self.d)]
        return '\n'.join(['Contact list', '------------'] + sorted_list)
