# Demonstrate encapsulation by creating private attributes (A/c No, 	balance) for a BankAccount class and providing getter and setter methods.
class BankAccount:
    def __init__(self, acc_no, balance):
        self.__acc_no = acc_no
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,balance):
        self.__balance = balance
        
    def get_acc_no(self):
        return self.__acc_no
    
    def set_acc_no(self,acc_no):
        self.__acc_no = acc_no
        
account1=BankAccount(1,10000)
account2=BankAccount(2,20000)
print(account1.get_acc_no())
print(account2.get_acc_no())
account1.set_balance(2000)
account2.set_balance(1000)
print(account1.get_balance())
print(account2.get_balance())