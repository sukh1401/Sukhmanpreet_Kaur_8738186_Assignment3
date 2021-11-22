
class BankSystem:
    balance = 0

    def __init__(self):
        amount = float(input("Enter initial deposit amount: "))
        self.balance = amount
        self.displayBalance()
        self.runUserTasks()

    def runUserTasks(self):
        operation = input("Enter operation to perform:(deposit/withdraw) ")
        if(operation == "deposit"):
            self.deposit()
        elif(operation == "withdraw"):
            self.withdraw()
        else:
            print("Invalid operation")
        self.displayBalance()

    def deposit(self):
        amount = float(input("Enter amount to be deposited: $ "))
        self.balance += amount

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: $"))
        if(self.balance >= amount):
            self.balance -= amount
            print("You withdrew $%.2f from the account" % amount)
        else:
            print("Insufficient funds")

    def displayBalance(self):
        print("Available balance: $%.2f" % self.balance)

if __name__ == '__main__':    
    # Bank system
    print(" Bank system")
    bankSystem = BankSystem()
    print("====================================")