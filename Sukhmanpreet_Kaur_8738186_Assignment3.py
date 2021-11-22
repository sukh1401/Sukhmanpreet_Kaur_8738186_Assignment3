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





if __name__ == '__main__':
    # Order System
    orderSystem = OrderSystem()
    orderSystem.run()

    # Factorial Program
    factorialCalculator = Factorial()
    factorialCalculator.run()

   