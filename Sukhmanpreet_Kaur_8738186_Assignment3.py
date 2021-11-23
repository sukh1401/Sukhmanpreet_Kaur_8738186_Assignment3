from datetime import datetime


class PoloShirts():
    name = 'Polo Shirt'
    quantity = 0
    color = ''

    def __init__(self,  color, quantity):
        self.quantity = quantity
        self.color = color

    def __str__(self):
        return self.name


class TShirts():
    name = 'T-Shirt'
    quantity = 0
    color = ''

    def __init__(self,  color, quantity):
        self.quantity = quantity
        self.color = color

    def __str__(self):
        return self.name


class Calculate:
    def calcTotal(self, quantity, price):
        return round((quantity * price), 2)

    def calcHST(self, totalCost):
        return round(((13/100) * totalCost), 2)

    def calTotalPayable(self, totalCost, hst):
        return round((totalCost + hst), 2)


class OrderSystem:
    company = "=====    Abby's Merchandizing (AM)    ======"
    welcomeMessage = "== Welcome to our Online Shirt Orders Shop!!! =="
    dateOfOrder = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    totalCost = 0
    totalPayable = 0
    CONSTANT_PRICE = 9.99
    product = None

    def run(self):
        print(self.company)
        print(self.welcomeMessage)
        self.getUserInputs()
        calculator = Calculate()
        self.totalCost = calculator.calcTotal(
            self.product.quantity, self.CONSTANT_PRICE)
        self.hst = calculator.calcHST(self.totalCost)
        self.totalPayable = calculator.calTotalPayable(
            self.totalCost, self.hst)
        self.printReceiptSummary()

    def getUserInputs(self):
        color = input("Which color of shirt do you want to order: ")
        typeOfShirt = int(
            input("Which shirt do you want? (Enter 1 for Polo, 2 for Shirt): "))

        quantity = int(input("How many shirts do you want?: "))

        if(typeOfShirt == 1):
            self.product = PoloShirts(color, quantity)
        elif typeOfShirt == 2:
            self.product = TShirts(color, quantity)
        else:
            print("Please enter a valid type of shirt option:")
            quantity = 0
            color = None
            typeOfShirt = None
            self.getUserInputs()
        if quantity < 1:
            print("Quantity should be greater than zero")
            quantity = 0
            color = None
            typeOfShirt = None
            self.getUserInputs()

    def printReceiptSummary(self):

        summary = f"""
                      Receipt       {self.dateOfOrder}
                _________________________________
                    {self.company}
            ______________________________________________________________
            Description                 Qty          Price            Total
            ______________________________________________________________
            {self.product.color} {self.product.name}                 {self.product.quantity}     x    ${self.CONSTANT_PRICE}        = ${self.totalCost}
            ______________________________________________________________
                TOTAL AMOUNT                                      ${self.totalPayable}

                Sub Total                                         ${self.totalCost}
                Harmonized Sales Tax                              ${self.hst}
                Balance                                           ${self.totalPayable}

                ||||||||||||||||||||||||||||||||
            """
        print(summary)

class Factorial:
    def factorial(self, value):

        product = 1
        for i in range(1, value+1):
            product *= i
        return product

    def getUserInputs(self):
        value = int(input("Enter a number: "))
        return value

    def run(self):
        number = self.getUserInputs()
        result = self.factorial(number)
        print(f"The factorial of {number} is {result}")




class LargestValue:
    def maxValue(self, first, second, third):
        maximumNumber = 0
        if(first >= second and first >= third):
            maximumNumber = first
        if (second >= first and second >= third):
            maximumNumber = second
        if (third >= first and third >= second):
            maximumNumber = third
        return maximumNumber

    def getUserInputs(self):
        first = int(input("Enter first number: "))
        second = int(input("Enter second number: "))
        third = int(input("Enter third number: "))
        return (first, second, third)

    def run(self):
        first, second, third = self.getUserInputs()
        maximumNumber = self.maxValue(first, second, third)
        print(f"Maximum of {first},{second},{third} is => {maximumNumber}")


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
    # Order System
    print("Order System")
    orderSystem = OrderSystem()
    orderSystem.run()
    print("========================================")

    # Factorial Program
    print("Factorial Program")
    factorialCalculator = Factorial()
    factorialCalculator.run()
    print("========================================")
    

    # Maximum of three finder
    print("Maximum of three finder")
    largestValueFinder = LargestValue()
    largestValueFinder.run()
    print("========================================")

    # Bank system
    print("Bank system")
    bankSystem = BankSystem()