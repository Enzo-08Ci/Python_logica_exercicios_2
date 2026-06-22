class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Depósito
    def deposit(self, amount):
        print(f'Deposit: {amount}')
        self.balance += amount
        self.show_balance()

    # Saque
    def withdraw(self, amount):
        print(f'Withdraw: {amount}')

        # Testa se saque é permitido
        if amount <= self.balance:
            self.balance -= amount
            self.show_balance()
        else:
            print("    Saldo insuficiente!")

    # Retorna o saldo atual
    def show_balance(self):
        print(f'--- {self.owner} ---')
        print(f'Balance: {self.balance}\n')

ac1 = BankAccount("Joca", 1000.0)

print('\n')

# Mostra saldo
ac1.show_balance()

# Depositando
ac1.deposit(1500.0)

# Retirada
ac1.withdraw(2000.0)

# Retirada
ac1.withdraw(600)