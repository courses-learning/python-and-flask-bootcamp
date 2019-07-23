####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, x):
        self.balance += x
        print(f'Deposit: {x}, Current balance: £{self.balance}')

    def withdraw(self, x):
        if self.balance - x < 0:
            print(f'You have insufficiant funds to withdraw £{x}.')
            return
        else:
            self.balance -= x
        print(f'Withdrawl: {x}, Current balance: £{self.balance}')

    def __repr__(self):
        return f'Account name: {self.owner}, Balance: {self.balance}'


# 1. Instantiate the class
acct1 = Account('Jose', 100)


# 2. Print the object
print(acct1)


# 3. Show the account owner attribute
acct1.owner


# 4. Show the account balance attribute
acct1.balance


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)


acct1.withdraw(75)


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


# ## Good job!
