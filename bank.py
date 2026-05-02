def account_list_creation(supported_accounts):
    return [None] * supported_accounts

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