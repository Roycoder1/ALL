class AtmAccount:
    available_account = 9941

    def __init__(self,holder) -> None:
        self.__holder=holder

        self.account_number = AtmAccount.available_account
        available_account += 1
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance (self,amount):
        self.__balance +=amount
    def deposit(self,amount):
        self.__balance +=amount
    def withdraw (self,amount):
        if amount>self.balance:
            raise ValueError("Insufficient funds")
            self._balance+= -amount

# account1 = AtmAccount("Yossi Eik")
account1.deposit(100)

print(account1.account_number)


