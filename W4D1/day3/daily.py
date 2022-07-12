# # Daily challenge

# # Challenge1 :

# from pickletools import dis


# user_word = input("Gimme a word")
# dictionnary = {}

# for letter in range(len(user_word)):
#     if user_word[letter] not in dictionnary:
#         dictionnary[user_word[letter]] = [letter]
#     else:
#         dictionnary[user_word[letter]].append(letter)

# print(dictionnary)

# The key is the product, the value is the price


items_purchase = {
  "Water": "1",
  "Bread": "3",
  "TV": "1000",
  "Fertilizer": "20"
}
# int(items_purchase.values)
wallet0 = "300"
wallet0= int(wallet0)
print(type(wallet0))
print(items_purchase.values)

for product,price in items_purchase.items():
   
    if int(price) <wallet0 :
        budget = (f'you can afford :{product,int(price)}' )
        print(budget+'$')
    else :
        overBudget = (f'{product,int(price)} not enough money')
        print (overBudget)
        





items_purchase2 = {
  "Apple": "4",
  "Honey": "3",
  "Fan": "14",
  "Bananas": "4",
  "Pan": "100",
  "Spoon": "2"
}

wallet1 = "100" 
wallet1= int(wallet1)
print(type(wallet1))
print(items_purchase2.values)

for product,price in items_purchase2.items():
   
    if int(price) <wallet1 :
        budget1 = (f'you can afford :{product,float(int(price))}' )
        print(budget1+'$')
    
    
        



items_purchase3 = {
  "Phone": "999",
  "Speakers": "300",
  "Laptop": "5000",
  "PC": "1200"
}

wallet2 = "1" 

wallet2= int(wallet2)
print(type(wallet2))
print(items_purchase3.values)

for product,price in items_purchase3.items():
    print(str(product),str(price)+'$')
   
if float(int(price)) > wallet2 :
    print('nothing')

