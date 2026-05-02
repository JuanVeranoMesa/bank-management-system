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