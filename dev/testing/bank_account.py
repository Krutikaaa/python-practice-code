'''Encapsulation is the process of hiding the internal state of an object and requiring 
all interactions to be performed through an object’s methods. This approach:

Provides better control over data.
Prevents accidental modification of data.
Promotes modular programming.
Python achieves encapsulation through public, protected and private attributes.'''

class BankAccount:
    # __account_number and __balance are private attributes,
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
            print(f"{amount} is doposited")
        else:
            print(amount is 0)

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"{amount} is withdrawn")
        else:
            print("insufficent balance")

    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
        

account = BankAccount(balance = 555555, account_number= 123456789)