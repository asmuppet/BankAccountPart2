import BankAccountClass


class CheckingAccount(BankAccountClass.BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit):
        BankAccountClass.BankAccount.__init__(self, customer_name, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit
