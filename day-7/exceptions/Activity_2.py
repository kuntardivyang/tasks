# Create a custom exception class InsufficientBalanceError for a banking program.
# Use the logging module to log exceptions to a file instead of printing them to the console.
import logging

logging.basicConfig(filename="errors.log", 
                    format='%(asctime)s %(message)s',
                    filemode='a+')

logger = logging.getLogger()

class InsufficientBalanceError(Exception):
    """Exception raised for Insufficent balance in account ."""

    def __init__(self, message):
        super().__init__(message)

class NegativeAmountError(Exception):
    """Exception raised for Negative input amount ."""

    def __init__(self, message):
        super().__init__(message)
        
class BankAccount:
    def __init__(self):
        self.balance = 0
        
    def deposit(self):
            deposit_amount = float(input('Enter Amount to deposit : '))
            if deposit_amount < 0:
                raise NegativeAmountError('Amount cant be negative')
            self.balance += deposit_amount
            print('Amount Deposited')

    def withdraw(self):
            withdraw_amount = float(input('Enter Amount to withdraw : '))
            if withdraw_amount < 0 :
                raise NegativeAmountError('Amount cant be negative')
            if withdraw_amount > self.balance:
                raise InsufficientBalanceError("Insufficeient Balance in account")
            else:
                self.balance -= withdraw_amount
        
    def check_balance(self):
        print('Your Current Balance is : ', self.balance)
        
bankAccount_object = BankAccount()
try :
    bankAccount_object.deposit()
    bankAccount_object.check_balance()
    bankAccount_object.withdraw()
    bankAccount_object.check_balance()
except ValueError as e:
    logger.error(e)
except InsufficientBalanceError as e:
    logger.error(e)
except NegativeAmountError as e:
    logger.error(e)