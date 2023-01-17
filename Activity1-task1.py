#Write a program to simulate bank transactions for two clients in a procedural paradigm. 
#The clients can deposit, withdraw and check their balance.

balance = 0

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
    else:
        print("Insufficient funds.")
        
def check_balance():
    global balance
    print("Your current balance is:", balance)


#First Client transaction 
deposit(100)
withdraw(50)
check_balance() #must print "Your current balance is: 50"

#Second Client Transaction
deposit(200)
withdraw(150)
check_balance()  #must print "Your current balance is: 50"
