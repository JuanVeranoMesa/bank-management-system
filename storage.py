import json
from account import Account


def save_accounts(bank):
    data = []

    for account in bank.account_list:
        if account is not None:
            data.append(account.to_dict())

    with open('accounts.json', 'w') as file:
        json.dump(data, file, indent=4)


def load_accounts(bank):
    try:
        with open('accounts.json', 'r') as file:
            data = json.load(file)

        for account_data in file:
            account = Account.from_dict(account_data)
            bank.add_account_to_bank(account)

    except FileNotFoundError:
        pass