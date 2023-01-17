# OOP Implementation
# Write a program to simulate bank transactions for two clients in a procedural paradigm. 
# The clients can deposit, withdraw and check their balance.


class BankAccount:
    def __init__(self):
        self.balance = 0  

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print("Your current balance is:", self.balance)

#First client
client_1 = BankAccount()
client_1.deposit(100)
client_1.withdraw(50)
client_1.check_balance() #prints "Your current balance is: 50"

#Second client
client_2 = BankAccount()
client_2.deposit(200)
client_2.withdraw(50)
client_2.check_balance() #prints "Your current balance is: 150"
