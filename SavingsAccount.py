import BankAccountClass


class SavingsAccount(BankAccountClass.BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, interest):
        BankAccountClass.BankAccount.__init__(self, customer_name, current_balance, minimum_balance)
        self.interest = interest
