class InsufficientFundsException(Exception):
    def __init__(self):
        self.message = "The Cash in your Account is Insufficient"
        super().__init__(self.message)


class InvalidAmountException(Exception):
    def __init__(self):
        self.message = "The Amount you Entered is Invalid"
        super().__init__(self.message)


class ATM:

    def __init__(self, cash):
        self.__cash = cash

    def withDraw(self, amount):

        if amount > self.__cash:

            raise InsufficientFundsException()
        elif amount <= 0:
            raise InvalidAmountException()
        else:
            print("Please Collect Your Cash-->", amount)
            self.__cash -= amount
            return "WithDraw Successfully"

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountException()
        else:
            self.__cash += amount
            return "Deposited Successfully"

    def getbalance(self):
        return "Your Balance is {}".format(self.__cash)


Ram = ATM(1000)

while 1:
    choice = int(input("""Enter your Choice
1.Withdraw
2.Deposit
3.Check Balance
4.Exit\n"""))
    if choice >= 4:
        print("Thank You")
        break
    if choice == 3:
        print(Ram.getbalance())
        continue
    cash = int(input("Enter Amount: "))
    try:
        if choice == 1:
            Ram.withDraw(cash)
        if choice == 2:
            Ram.deposit(cash)
        Query = int(input("Do you want to display Balance:\n1.Yes 2.No: "))
        if Query == 1:
            print(Ram.getbalance())
    except Exception as AtmException:
        print("""**************{}**************""".format(AtmException))
