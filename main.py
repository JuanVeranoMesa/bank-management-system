import random

from account import Account
from coin_collector import CoinCollector
from bank import Bank
from input_helpers import (
    get_pin,
    get_new_pin,
    get_user_account_number,
    get_string,
    get_amount,
    get_amount_multiple
)
from storage import save_accounts, load_accounts


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


def atm_calculation():
    amount = get_amount_multiple()
    amount_of_20 = amount // 20
    amount = amount % 20
    amount_of_10 = amount // 10
    amount = amount % 10
    amount_of_5 = amount // 5

    return amount_of_20, amount_of_10, amount_of_5


def bank_manager():
    current_input = None
    bank = Bank()
    load_accounts(bank)

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
                save_accounts(bank)

        if current_input == 2:
            account= prompt_for_account_number_and_pin(bank)
            if account is not None:
                print(account)
        
        if current_input == 3:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                change_pin(account)    
                save_accounts(bank)  

        if current_input == 4:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                account.deposit(get_amount('deposit'))
                print(f'New balance: ${account.balance:,.2f}')
                save_accounts(bank)

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
                save_accounts(bank)
            else:
                print(f'Insufficient funds in account {account_1.account_number}')

        if current_input == 6:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                account.withdraw(get_amount('withdraw'))
                print(f'New balance: ${account.balance:,.2f}')
                save_accounts(bank)

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
                    save_accounts(bank)

        if current_input == 8:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                coin_count = CoinCollector()
                coin_input = input('Deposit coins:\n')
                account.deposit(coin_count.parse_change(coin_input))
                print(f'Invalid coins: {''.join(coin_count.rejected_change)}')
                print(f'New balance: {account.balance:,.2f}')
                save_accounts(bank)
        
        if current_input == 9:
            account = prompt_for_account_number_and_pin(bank)
            if account is not None:
                print(f'Account {account.account_number} closed')
                bank.remove_account_from_bank(account)
                save_accounts(bank)
        

if __name__ == '__main__':
    bank_manager()