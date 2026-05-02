class Account:
    def __init__(self, account_number, owner_first_name, owner_last_name, pin, balance):
        self.account_number = account_number
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient funds in account {self.account_number}')
            return self.balance
        self.balance -= amount
        return self.balance

    def is_valid_pin(self, pin):
        return self.pin == pin
    
    def __str__(self):
        self_info = '\n============================================================\n'
        self_info += f'Account Number: {self.account_number}\n'
        self_info += f'Owner First Name: {self.owner_first_name}\n'
        self_info += f'Owner Last Name: {self.owner_last_name}\n'
        self_info += f'Balance: ${self.balance:,.2f}\n'
        self_info += '============================================================\n'
        return self_info
