import random


def draw_main():
    print('============================================================')
    print('What do you want to do?')
    print('1. Open an account')
    print('2. Get account information and balance')
    print('3. Change PIN')
    print('4. Deposit money in account')
    print('5. Transfer money between accounts')
    print('6. Withdraw money from account')
    print('7. ATM withdrawal')
    print('8. Deposit change')
    print('9. Close an account')
    print('10. End program')
    print('============================================================')


def account_list_creation(supported_accounts):
    return [None] * supported_accounts


def account_creation(bank):
    account_number = account_number_creation(bank)
    first_name = get_string('first name')
    last_name = get_string('last name')
    pin = pin_creation()
    balance = 0.0
    return account_number, first_name, last_name, pin, balance


def account_number_creation(bank):
    new_account_number = random.randint(10000000, 99999999)
    for account in bank.account_list:
        if account is None:
            continue
        elif account.account_number == new_account_number:
            return account_number_creation(bank)
    
    return new_account_number


def pin_creation():
    pin = ''
    for _ in range(4):
        pin += str(random.randint(0,9))
    return pin


def prompt_for_account_number_and_pin(bank):
    account_input = get_user_account_number()
    account = bank.find_account(account_input)
    if account is not None:
        user_pin = get_pin()
        if account.is_valid_pin(user_pin):
            return account
        else:
            print('Invalid PIN')
            return None
    print(f'Account not found for account number: {account_input}')
    return None


def change_pin(account):
    while True:
        new_pin = get_new_pin(1)
        new_pin_confirmation = get_new_pin(2)
        if new_pin == new_pin_confirmation:
            account.pin = new_pin
            break
        else:
            print('PINs do not match, try again.')
        

def get_pin():
    user_pin = ''
    while len(user_pin) != 4:
        try:
            user_pin = input('Enter PIN:\n')
            int(user_pin)
            if len(user_pin) != 4:
                print('PIN must be 4 digits, try again')
                continue
        except ValueError:
            print(f'{user_pin} is not a number.')
            user_pin = ''
            continue
    return user_pin


def get_new_pin(state):
    user_pin = ''
    if state == 1:
        while len(user_pin) != 4:
            try:
                user_pin = input('Enter new PIN:\n')
                int(user_pin)
                if len(user_pin) != 4:
                    print('PIN must be 4 digits, try again')
                    continue
            except ValueError:
                print(f'{user_pin} is not a number.')
                user_pin = ''
                continue
        return user_pin
    if state == 2:
        while len(user_pin) != 4:
            try:
                user_pin = input('Enter new PIN again to confirm:\n')
                int(user_pin)
                if len(user_pin) != 4:
                    print('PIN must be 4 digits, try again')
                    continue
            except ValueError:
                print(f'{user_pin} is not a number.')
                user_pin = ''
                continue
        return user_pin       


def get_user_account_number():
    account_input = 0

    while account_input < 10000000 or account_input > 99999999:
        try:
            account_input = int(input('Please enter your 8 digit account number:\n'))
        except ValueError:
            print('Account must only be an 8 digit number.')
            continue
    
    return account_input


def get_string(info_type):
    user_string = ''
    user_input = '0'

    while user_input != '1':
        user_string = input(f'\nPlease enter your {info_type}: \n')
        user_input = input(f'If {user_string} is correct, please press 1, otherwise input anything to retype: \n')
    
    return user_string


def get_amount(info_type):
    amount = None
    user_input = None

    while user_input != '1':
        try:
            amount = round(float(input(f'\nEnter amount to {info_type} in dollars and cents(e.g. 2.57): \n')), 2)
            if amount < 0:
                print('The amount cannot be negative. Try again.')
                continue
            if amount == 0:
                print('The amount cannot be zero. Try again.')
                continue
        except ValueError:
            print('Please input a numerical amount.')
            continue
        
        user_input = input(f'If ${amount:,.2f} is correct, please press 1, otherwise input anything to retype: \n')

    return amount


def get_amount_multiple():
    amount = 1
    
    while amount % 5 != 0:
        try:
            amount = int(input('Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000):\n'))
            if amount < 5 or amount > 1000 or amount % 5 != 0:
                print('Invalid amount. Try again.')
                amount = 1
        except ValueError:
            print('Input must be an integer from 1 to 1000. Try again.')
    
    return amount


def atm_calculation():
    amount = get_amount_multiple()
    amount_of_20 = amount // 20
    amount = amount % 20
    amount_of_10 = amount // 10
    amount = amount % 10
    amount_of_5 = amount // 5

    return amount_of_20, amount_of_10, amount_of_5


class Bank:
    supported_accounts = 100
    def __init__(self):
        self.account_list = account_list_creation(Bank.supported_accounts)

    def add_account_to_bank(self, account):
        for i in range(len(self.account_list)):
            if self.account_list[i] is None:
                self.account_list[i] = account
                return True
            
        print('\nNo more accounts available')
        return False

    def remove_account_from_bank(self, account_to_remove):
        for i in range(len(self.account_list)):
            if self.account_list[i] is not None:
                if self.account_list[i].account_number == account_to_remove.account_number:
                    self.account_list[i] = None
                    break
                
    def find_account(self, account_number):
        for i in range(len(self.account_list)):
            if self.account_list[i] is not None:
                if self.account_list[i].account_number == account_number:
                    return self.account_list[i]

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

class CoinCollector:
    def __init__(self):
        self.penny = 0
        self.nickel = 0
        self.dime = 0
        self.quarter = 0
        self.half_dollar = 0
        self.whole_dollar = 0
        self.rejected_change = []

    def parse_change(self, change):
        split_change = list(change)
        for char in split_change:
            if char == 'P':
                self.penny += 1
            elif char == 'N':
                self.nickel += 1
            elif char == 'D':
                self.dime += 1
            elif char == 'Q':
                self.quarter += 1
            elif char == 'H':
                self.half_dollar += 1
            elif char == 'W':
                self.whole_dollar += 1
            else:
                self.rejected_change.append(char)
        
        return(self.calculate_amount())

    def calculate_amount(self):
        amount = self.penny * .01
        amount += self.nickel * .05
        amount += self.dime * .1
        amount += self.quarter * .25
        amount += self.half_dollar * .5
        amount += self.whole_dollar

        print(f'${amount:,.2f} in coins deposited into account')
        return amount


def bank_manager():
    current_input = None
    bank = Bank()

    while current_input != 10:
        draw_main()
        current_input = None

        try:
            current_input = int(input('Please input selection: ')) 
            if current_input < 1 or current_input > 10:
                print('Input not in range.')
        except ValueError:
            print('Input must be an integer from the list.')

        if current_input == 1:
            account = Account(*account_creation(bank))
            if bank.add_account_to_bank(account) == True:
                print(account)
                print(f'Your new account pin is: {account.pin}')

        if current_input == 2:
            account= prompt_for_account_number_and_pin(bank)
            if account is not None:
                print(account)
        
        if current_input == 3:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                change_pin(account)      

        if current_input == 4:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                account.deposit(get_amount('deposit'))
                print(f'New balance: ${account.balance:,.2f}')

        if current_input == 5:
            print('Account to Transfer From:')
            account_1 = prompt_for_account_number_and_pin(bank)
            if account_1 is None:
                continue
            print('Account to Transfer To:')
            account_2 = prompt_for_account_number_and_pin(bank)
            if account_2 is None:
                continue
            transfer_amount = get_amount('transfer')
            if account_1.balance >= transfer_amount:
                account_1.withdraw(transfer_amount)
                account_2.deposit(transfer_amount)
                print(f'New balance in account {account_1.account_number}: ${account_1.balance:,.2f}')
                print(f'New balance in account {account_2.account_number}: ${account_2.balance:,.2f}')
                print('Transfer Complete')
            else:
                print(f'Insufficient funds in account {account_1.account_number}')

        if current_input == 6:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                account.withdraw(get_amount('withdraw'))
                print(f'New balance: ${account.balance:,.2f}')

        if current_input == 7:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                previous_balance = account.balance
            while account is not None:
                if account.balance < 5:
                    print('Insufficient funds for transaction.')
                    break
                amount_20, amount_10, amount_5 = atm_calculation()
                account.withdraw(amount_20 * 20 + amount_10 * 10 + amount_5 * 5)
                if previous_balance == account.balance:
                    continue
                break
            if account is not None: 
                if previous_balance != account.balance:
                    print(f'Number of 20-dollar bills: {amount_20}') 
                    print(f'Number of 10-dollar bills: {amount_10}')
                    print(f'Number of 5 dollar bills: {amount_5}')
                    print(f'New balance: {account.balance:,.2f}')

        if current_input == 8:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                coin_count = CoinCollector()
                coin_input = input('Deposit coins:\n')
                account.deposit(coin_count.parse_change(coin_input))
                print(f'Invalid coins: {''.join(coin_count.rejected_change)}')
                print(f'New balance: {account.balance:,.2f}')
        
        if current_input == 9:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                print(f'Account {account.account_number} closed')
                bank.remove_account_from_bank(account)
        

bank_manager()