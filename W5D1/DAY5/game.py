# Part I - Game.Py
# game.py – this file/module should contain a class called Game. It should have 4 methods:
# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# Get the user’s item (rock/paper/scissors) and remember it

# Get a random item for the computer (rock/paper/scissors) and remember it

# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
import random
class Game():
     
    def __init__(self) -> None:
        pass

    def get_user_item(self):
        user = input("Choose between Rock, paper and scissors to play")
        # print (user)
        
        rock = 'rock'
        paper = 'paper'
        scissors = 'scissors'
        while True:
            if user == rock or user == paper or user == scissors:
                break
            else:
                user = input("Choose Rock, paper or scissors !!!")
        return user
    def get_computer_item(self):
        rock = 'rock'
        paper = 'paper'
        scissors = 'scissors'
        list = [rock,paper,scissors]
        
        random1 = random.choice(list)
        # print(random1)
        return random1
    
    def get_game_result(self, user_item, computer_item):
        
        rock = 'rock'
        paper = 'paper'
        scissors = 'scissors'
        if user_item==rock and computer_item == paper:
            print ("you choosed rock , computer won")
        if user_item==paper and computer_item == paper:
            print ("you choosed paper , tie")
        if user_item==scissors and computer_item == paper:
            print ("you choose scissors , you won")
        if user_item==rock and computer_item == scissors:
            print ('you choosed rock , you won')
        if user_item==rock and computer_item == rock:
            print ('you choosed rock , tie')
        if user_item==paper and computer_item == rock:
            print ('you choosed paper , you won')
        if user_item==paper and computer_item == scissors:
            print ("you choose paper , computer won")
        if user_item==scissors and computer_item == scissors:
            print ("you cjoosed scissors , tie")
        if user_item==scissors and computer_item == rock:
            print ("You choosed scissors, computer won")
    
    def play(self,user_item,computer_item):
        
        rock = 'rock'
        paper = 'paper'
        scissors = 'scissors'
        remember= res
        print(remember)
        rememberRandom = res2
        print(rememberRandom)
        condition =res3
        
        win = 0
        draw = 0
        loss = 0
        
        if user_item==rock and computer_item == paper:
            loss+=1
            print(f"lose:{loss}")
        if user_item==paper and computer_item == paper:
            draw+=1
            print(f"draw:{draw}")
        if user_item==scissors and computer_item == paper:
             win+=1
             print(f"win:{win}")
        if user_item==rock and computer_item == scissors:
             win+=1
             print(f"win:{win}")
        if user_item==rock and computer_item == rock:
              print(f"draw:{draw}")
        if user_item==paper and computer_item == rock:
              win+=1
              print(f"win:{win}")
        if user_item==paper and computer_item == scissors:
              loss+=1
              print(f"lose:{loss}")
        if user_item==scissors and computer_item == scissors:
              print(f"draw:{draw}")
        if user_item==scissors and computer_item == rock:
              loss+=1
              print(f"lose:{loss}")
        
        

        



game1 = Game()
# game1.get_user_item()
# game1.get_computer_item()
res = game1.get_user_item()
res2 = game1.get_computer_item()
res3 = game1.get_game_result(res,res2)
# game1.get_game_result(res,res2)
game1.play(res,res2)

