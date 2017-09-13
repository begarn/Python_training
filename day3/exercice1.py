#! /usr/bin/env python3
# -*- coding : UTF-8 -*

class BankAccount:
    def __init__(self, name = 'Dupont', sold = 1000):
        self.name = name
        self.sold = sold

    def __str__(self):
        return 'Name: ' + self.name + '\n' + 'Sold: ' + str(self.sold)

    def depot(self, amount):
        self.sold += amount

    def retrait(self, amount):
        self.sold -= amount

def main():
    account1 = BankAccount('Duchmol', 800)
    print(account1)
    account1.depot(350)
    account1.retrait(200)
    print(account1)

    account2 = BankAccount()
    account2.depot(25)
    print(account2)

if __name__ == '__main__':
    main()
