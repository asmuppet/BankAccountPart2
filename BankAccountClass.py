import random
class BankAccount():

    bank_title = "Bank of Bolivia"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.__account_number = random.randint(10000, 99999)
        self._routing_number = random.randint(10000, 99999)

    def deposit(self, deposit_amount):
        self.current_balance += deposit_amount
        print(f"${deposit_amount:.2f} deposited.")

    def withdraw(self, withdraw_amount):
        if self.current_balance - withdraw_amount >= self.minimum_balance:
            self.current_balance -= withdraw_amount
            print(f"${withdraw_amount:.2f} withdrawn.")

        else:
            print(f"This withdrawal of ${withdraw_amount:.2f} will not process as it will cause the account balance to "
                  f"drop below the minimum balance of ${self.minimum_balance:.2f}.")

    def print_customer_information(self):
        print(f"This is the account of {self.customer_name}, a customer of {self.bank_title}. It has a minimum balance "
              f"of ${self.minimum_balance:.2f} and the current balance is ${self.current_balance:.2f}.")
