# I part - creating class
from turtle import st
from typing_extensions import Self


class BankAccount:

    def __init__(self, name: str, number: int, balance: float) -> Self:
        self.holder = name
        self.number = number
        self.balance = balance

    def deposit(self, amount:float):
        if amount > 0:
            self.balance += amount
    
# II part - creating class with inheritance

class BankAccount:

    def __init__(self, name: str, number: int, balance: float) -> Self:
        self.holder = name
        self.number = number
        self.balance = balance

    def deposit(self, amount:float):
        if amount > 0:
            self.balance += amount

class StudentAccount(BankAccount):

    def __init__(self, name: str, number: int, balance: float, student_id: str) -> Self:
        super().__init__(name, number, balance)
        self.student_id = student_id
    
# part III decorators

class BankAccount:

    def __init__(self, name: str, number: int, balance: float) -> Self:
        self._holder = name # _ protected
        self.__number = number # __ private
        self._balance = balance 

    @property
    def holder(self):
        return self._holder

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self._balance = amount        

class StudentAccount(BankAccount):

    def __init__(self, name: str, number: int, balance: float, student_id: str) -> Self:
        super().__init__(name, number, balance)
        self.student_id = student_id






# part IV dunder methods
class BankAccount:

    def __init__(self, name: str, number: int, balance: float) -> Self:
        self._holder = name # _ protected
        self.__number = number # __ private
        self._balance = balance 

    @classmethod
    def from_dict(cls, dict_values):
        new_instance = BankAccount(*dict_values)
        return new_instance

    @property
    def holder(self):
        return self._holder

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self._balance = amount        

    def __iadd__(self, amount): # +=
        self._balance += amount
        return self
    
    def __str__(self):
        pass

    def __repr__(self):
        return str(self.__dict__)

    def info(self):
        out = f"""
            {self.holder}
            {self.balance}
            """
        print(out)
class StudentAccount(BankAccount):

    def __init__(self, name: str, number: int, balance: float, student_id: str) -> Self:
        super().__init__(name, number, balance)
        self.student_id = student_id


class Student:

    def __init__(self, name: str) -> Self:
        self.name = name

    def info(self):
        out = f"""
            {self.name}
            """
        print(out)

class Employee:

    def __init__(self, name: str , site: str) -> Self:
        self.name = name
        self.site = site

    def info(self):
        out = f"""
            {self.name}
            {self.site}
            """
        print(out)    


student_account_brad = StudentAccount('Brad', 82734, 100.0, 13213)
student_brad = Student('Brad')
employee_brad = Employee('Brad', 'Construction')

# Polymorphism
items = [student_account_brad, student_brad, employee_brad]

for item in items: 
    item.info()

