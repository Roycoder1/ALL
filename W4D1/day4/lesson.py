# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

# def calculation(addition, substraction):
#    sub1 = addition-substraction
#    add1 = addition+substraction
#    return sub1 , add1

# res , deli = calculation(12,5)
# print('Substraction:',res)
# print('Addition :' , deli )


from unicodedata import name


people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

say = lambda name : True if len(name)<=4 else False

print(list(filter(say , people )))

def sayHello (name):
    hello = say()+ "Hello"
    return hello
print(list(sayHello))