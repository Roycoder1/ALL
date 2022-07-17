# # from sre_constants import CH_LOCALE


# # class Character ():
# #  characters_created = 0
# #  characters = {}
   
# #     def __init__(self,name,age , strenght,defense):
# #         self.name = name
# #         self.age = age
# #         self.strenght = strenght
# #         self.defense=defense
# #         Character.characters_created +=1
# #         Character.characters[self.name] = self

# # conan = Character("roger",21,200,300)

# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# class CharacterTraits:
#     def __init__(self, strength:int, intelligence:int, dexterity:int, character_class:str, defence:str):
#         self.strength = strength
#         self.intelligence = intelligence
#         self.dexterity = dexterity
#         self.character_class = character_class
#         self.defence = defence
        
# class RPG_CHARACTER:
#     """Class for creating RPG character"""
#     characters_created = 0
#     characters = {}
#     def __init__(self, name:str, traits = (0,0,0,"None",0)) -> object:
#         self.name = name
#         self.traits = CharacterTraits(*traits)
#         RPG_CHARACTER.characters_created += 1
#         RPG_CHARACTER.characters[self.name] = self
#     def move(self) -> None:
#         print(self.name + " moves")
#     def print_characters():
#         pp.pprint(RPG_CHARACTER.characters)
#     def strike(self)->None:
        
# conan = RPG_CHARACTER("Conan", traits = (100, 150, 120, "Warrior", 300))
# zina = RPG_CHARACTER("Zina", traits = (100, 150, 120, "Warrior", 300))
# RPG_CHARACTER.print_characters()
# RPG_CHARACTER.strike("fire")

# Exercise1:
# from multiprocessing.pool import ApplyResult


# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("Hello my name is " + self.name)

# first_person = Person("John", 36)
# first_person.show_details()

# # Expected output = Hello my name is John

# class Computer():

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")
# Expectet output : 
# self = None
# "Apple"
# "I am a computer my name is Mark"

# class BankAccount:

#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#         self.transactions = []

#     def view_balance(self):
#         self.transactions.append("View Balance")
#         print(f"Balance for account {self.account_number}: {self.balance}")

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#         elif amount < 100:
#             print("Minimum deposit is 100")
#         else:
#             self.balance += amount
#             self.transactions.append(f"Deposit: {amount}")
#             print("Deposit Succcessful")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Funds")
#         else:
#             self.balance -= amount
#             self.transactions.append(f"Withdraw: {amount}")
#             print("Withdraw Approved")
#             return amount

#     def view_transactions(self):
#         print("Transactions:")
#         print("-------------")
#         for transaction in self.transactions:
#             print(transaction)


from collections import namedtuple
from time import sleep
import random
import pprint
Traits = namedtuple("Traits", "strength intelligence dexterity character_class defence")
pp = pprint.PrettyPrinter(indent=4)
class CharacterTraits:
    def __init__(self, strength:int, intelligence:int, dexterity:int, character_class:str, defence:str):
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.character_class = character_class
        self.defence = defence
class RPG_CHARACTER:
    """Class for creating RPG character"""
    characters_created = 0
    characters = {}
    def __init__(self, name:str, traits = Traits(0,0,0,‘None’,0)) -> object:
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_next_level = 100
        self.traits = CharacterTraits(*traits)
        RPG_CHARACTER.characters_created += 1
        RPG_CHARACTER.characters[self.name] = self
    def move(self) -> None:
        print(self.name + ' moves')
    def level_up(self):
        self.level += 1
    def set_next_levelXP(self):
        self.xp_next_level += self.level * self.xp_next_level
    def checkXP(self):
        if self.xp >= self.xp_next_level:
            self.level_up()
            self.set_next_levelXP()
            print(f”{self.name} is Leveled UP! Now level is {self.level}“)
        else:
            pass
    def strike(self) -> None:
        print(self.name + ' Is striking')
        self.xp += 5
        self.checkXP()
    def defence(self) -> None:
        print(self.name + ' Is defending')
        self.xp += 2
        self.checkXP()
    def print_characters():
        pp.pprint(RPG_CHARACTER.characters)
zina = RPG_CHARACTER(“Zina”, traits = (100, 150, 120, ‘Warrior’, 300))
def main():
    choices = [‘strike’, ‘defence’, ‘move’]
    conan = RPG_CHARACTER(“Conan”, traits = (100, 150, 120, ‘Warrior’, 300))
    while conan.level < 3:
        action = random.choice(choices)
        if action == ‘strike’:
            conan.strike()
        if action == ‘defence’:
            conan.defence()
        if action == ‘move’:
            conan.move()
        sleep(0.1)
main()