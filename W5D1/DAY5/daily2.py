# Instructions
# Part 1 : Quizz :
# Answer the following questions

# # What is a class?
# A class is a code template for creating objects.An object is created using the constructor of the class.
# # What is an instance?
# An instance is an object that belong to the class
# # What is encapsulation?
# Its a method that allow to put data in private or to protect them
# # What is abstraction?
# Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. 
# # What is inheritance?
# Its a method that allow to inherit of another class property
# # What is multiple inheritance?
# Multiple inheritance is two classes or more that give their properties to another derived class
# # What is polymorphism?
# Polymorphism defines the ability to take different forms. Polymorphism in Python allows us to define methods in the child class with the same name as defined in their parent class. 
# # What is method resolution order or MRO?
# It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance. In Python, the MRO is from bottom to top and left to right.

# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
import random
class Card():
    def __init__(self) -> None:
        pass
    def card(self):
        list =[]
        
        symbols = ['Spades','Hearts', 'Diamonds', 'Clubs']
        cardsNumber = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        for value,i in enumerate(cardsNumber):
            # list.append(i)
            print (i)
            for j in symbols:
                # list.append(i)
                # list.append(j)
                list2 = [i,j]
            
                # print(list2)
                
        return list2
        
        

        
        
        # print (list)

class Deck():
    def shuffle(self):
        res1 = card.card()
        print(res1)
        play = random.shuffle(res1)
        




       
        


card = Card()
card.card()
deck = Deck()
deck.shuffle()


