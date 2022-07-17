import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
print(word)
lista = []

guess = input("choose a letter")
print(len(word)*"_")

for i in word:  
    res1=[i]
    
    print(res1)
    if guess == i :
        res = list(guess)
        print(type(res))
        lista.append(res)
        print(lista)

