class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = float(balance)


data = input()
accounts = []

while not data == 'end':
    name = data.split(" | ")[1]
    bank = data.split(" | ")[0]
    balance = data.split(" | ")[2]

    account = BankAccount(balance=balance, name=name, bank=bank)
    accounts.append(account)

    data = input()

sorted_accounts = sorted(accounts, key=lambda acc: (-acc.balance, len(acc.bank)))

for account in sorted_accounts:
    print(f'{account.name} -> {account.balance:.2f} ({account.bank})')