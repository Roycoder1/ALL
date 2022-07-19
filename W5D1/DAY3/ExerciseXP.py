# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

# user = input ("Gimme a number")
# print(user)
# user = int(user)
# print (type(user))
# print (user)
# user = abs(user+4j)
# print (user)
# doc = user.__doc__
# print (doc)
# # Here i used input method to allow the user to input a number
# Then, i converted the input in number(int)
# Finally i used abs()function to get the absolute value of my number

# 🌟 Exercise 2: Currencies

# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

from locale import currency


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self) -> str:
        return f'{self.amount} {self.currency}'

    def __repr__(self) -> str:
        return f'{self.amount} {self.currency}'
    
    




c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

string = c1.__str__()
print (string)
c1_Int = int(c1.amount)
print (c1_Int)
repr = c1.__repr__()
print (repr)
print(c1_Int+5)
c2 = int(c2.amount)
print (c1_Int+c2)

print (f'{c1_Int} {c1.currency}')
c1_Int+=5
print (f'{c1_Int} {c1.currency}')
c1_Int +=c2
print(f'{c1_Int} {c1.currency}')

if c1.currency + c3.currency :
    raise ValueError(f"Cannot add between Currency type {c1.currency} and {c3.currency}")
print (c1.currency + c3.currency)