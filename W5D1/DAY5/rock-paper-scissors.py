# Create a new directory for the game. Inside it, create 2 files:
# rock-paper-scissors.py – this will contain functions to show the main menu, handle user’s input, and show the game summary before exiting.
# game.py – this will contain a Game class which will have functions to play a single game of rock-paper-scissors against the computer, determine the game’s result, and return the result.
from game import Game

class Menu():
    def get_user_menu_choice(self):
        newgame =  input("For a new game input newgame , to display score input display , to leave the game input quit ")
        if newgame == 'newgame':
            play1.get_user_item()
        if newgame == 'display':
            play1.play()
        if newgame == 'quit':
            return
        
    def print_results(self,result):
        
        print({play1.play()})
        

            

play1 = Game()
menu= Menu()

menu.get_user_menu_choice()
menu.print_results(play1.play())



