import SavingsAccount
import CheckingAccount

#user opens a savings account and deposits 100 dollars

SavingsAccount1 = SavingsAccount.SavingsAccount("Jimothy Smith", 0, -50, .075)

SavingsAccount1.print_customer_information()

SavingsAccount1.deposit(100)

SavingsAccount1.print_customer_information()

#user opens a checking account deposits 50 dollars then tries and fails to withdraw below the minimum

CheckingAccount1 = CheckingAccount.CheckingAccount("Delilah Cubings", 0, -25, 50)

CheckingAccount1.print_customer_information()

CheckingAccount1.deposit(50)

CheckingAccount1.print_customer_information()

CheckingAccount1.withdraw(100)

CheckingAccount1.print_customer_information()

#user opens a savings account with 100 dollars and withdraws too much

SavingsAccount2 = SavingsAccount.SavingsAccount("Timothy Smith", 100, 0, .05)

SavingsAccount2.print_customer_information()

SavingsAccount2.withdraw(101)

SavingsAccount2.print_customer_information()

#user opens a checking account with 500000 dollars then withdraws 10000

CheckingAccount2 = CheckingAccount.CheckingAccount("Christine Jones", 500000, -100, 250000)

CheckingAccount2.print_customer_information()

CheckingAccount2.withdraw(10000)

CheckingAccount2.print_customer_information()