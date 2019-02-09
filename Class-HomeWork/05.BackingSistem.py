from decimal import *

getcontext().prec = 2


class BankAccount:
    def __init__(self, name, bank, balance):
        self.__name = self.set_name(name)
        self.__bank = self.set_bank(bank)
        self.__balance = self.set_balance(balance)

    def set_name(self, name):
        if name.isalpha():
            return name

    def get_name(self):
        return self.__name

    def set_bank(self, bank):
        if bank.isalpha():
            return bank

    def get_bank(self):
        return self.__bank

    def set_balance(self, balance):
        if isinstance(balance,float):
            return balance

    def get_balance(self):
        return self.__balance


list_acaounts = []
while True:
    data = input()
    if data == 'end':
        break
    else:
        p_acaount = data.split(' | ')
        name_i = p_acaount[1]
        bank_i = p_acaount[0]
        balance_i = float(p_acaount[2])
        bankAc = BankAccount(name_i, bank_i, balance_i)
        list_acaounts.append(bankAc)

for a in list_acaounts:
    print(f'{a.get_name()} -> {a.get_balance():.2f} ({a.get_bank()})')
