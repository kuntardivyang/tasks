# Classes 
# Create a class to represent a BankAccount with methods to deposit, withdraw, and check balance.


class BankAccount:
    def __init__(self):
        self.balance = 0
        
    def deposit(self):
        try:
            deposit_amount = float(input('Enter Amount to deposit : '))
            self.balance += deposit_amount
            print('Amount Deposited')
        except ValueError:
            print('Enter ONLY Numeric Values')
        
    def withdraw(self):
        
        try:
            withdraw_amount = float(input('Enter Amount to withdraw : '))
            if withdraw_amount > self.balance:
                print('The Withdrawal Amount is greater then Current Bank Balance')
            else:
                self.balance -= withdraw_amount
        except ValueError:
            print('Enter ONLY Numeric Values')
            
    def check_balance(self):
        print('Your Current Balance is : ', self.balance)
        
bankAccount_object = BankAccount()
bankAccount_object.deposit()
bankAccount_object.check_balance()
bankAccount_object.withdraw()
bankAccount_object.check_balance()
print()