from ast import If
from cgitb import handler
from dataclasses import replace
from tkinter import HORIZONTAL
from turtle import position


print("Welcome to TIC TAC TOE")

print("TIC TAC TOE ")
moves = [1,2,3,4,5,6,7,8,9]
game_still_going = True
winner = None
current_player = "X"

def display_board():

    stars = "*"
    bars = "|"
    tirets = "-"
  
        
    board = [f"{moves[0]}",f"{moves[1]}",f"{moves[2]} ",
            "--","-","--",
             f"{moves[3]}",f"{moves[4]}",f"{moves[5]} ",
            "--","-","--",
             f"{moves[6]}",f"{moves[7]}", f"{moves[8]} "]
    print(stars*15+"         ")
    print("*"+"   "+board[0]+"|"+board[1]+"|"+board[2]+"    *")
    print("*"+"  "+board[3]+"|"+board[4]+"|"+board[5]+"    *")
    print("*"+"   "+board[6]+"|"+board[7]+"|"+board[8]+"    *")
    print("*"+"  "+board[9]+"|"+board[10]+"|"+board[11]+"    *")
    print("*"+"   "+board[12]+"|"+board[13]+"|"+board[14]+"    *")
    print(stars*15+"         ")
    # player_input(board)

# display_board()





def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner =="X"or winner =="O" :
     print(winner+"won")
    elif winner == None:
     print("Tie")

def handle_turn(player):
    playerColumn = input("Choose a number of a column ")
    playerRow = input("Choose a number of a row")

    if int(playerColumn)==1 and int(playerRow) ==1:
        var =  moves[0]="X"
        print (var)
        display_board()
        
        

    if int(playerColumn)==1 and int(playerRow) ==2:
        var1 =  moves[1]="X"
        print (var1)
        display_board()
        
        


    if int(playerColumn)==1 and int(playerRow) ==3:
        var2 =  moves[2]="X"
        print (var2)
        display_board()
        
        

    if int(playerColumn)==2 and int(playerRow) ==1:
        var3 =  moves[3]="X"
        print (var3)
        display_board()
        
        

    if int(playerColumn)==2 and int(playerRow) ==2:
        var4 =  moves[4]="X"
        print (var4)
        display_board()
        
        

    if int(playerColumn)==2 and int(playerRow) ==3:
        var5 =  moves[5]="X"
        print (var5)
        display_board()
        
        

    if int(playerColumn)==3 and int(playerRow) ==1:
        var6 =  moves[6]="X"
        print (var6)
        display_board()
        
        

    if int(playerColumn)==3 and int(playerRow) ==2:
        var7 =  moves[7]="X"
        print (var7)
        display_board()
        
        
    
    if int(playerColumn)==3 and int(playerRow) ==3:
        var8 =  moves[8]="X"
        print (var8)
        display_board()
       
        

        #Player2 moves:
    player2Column = input('Enter a column')
    player2Row = input("Enter a row")

    if int(player2Column)==1 and int(player2Row) ==2:
        var1 =  moves[1]="O"
        print (var1)
        display_board()
        


    if int(player2Column)==1 and int(player2Row) ==3:
        var2 =  moves[2]="O"
        print (var2)
        display_board()
        
        

    if int(player2Column)==2 and int(player2Row) ==1:
        var3 =  moves[3]="O"
        print (var3)
        display_board()
       

    if int(player2Column)==2 and int(player2Row) ==2:
        var4 =  moves[4]="0"
        print (var4)
        display_board()
        

    if int(player2Column)==2 and int(player2Row) ==3:
        var5 =  moves[5]="O"
        print (var5)
        display_board()
       

    if int(player2Column)==3 and int(player2Row) ==1:
        var6 =  moves[6]="O"
        print (var6)
        display_board()
        

    if int(player2Column)==3 and int(player2Row) ==2:
        var7 =  moves[7]="O"
        print (var7)
        display_board()
        
    
    if int(player2Column)==3 and int(player2Row) ==3:
        var8 =  moves[8]="O"
        print (var8)
        display_board()
        
 
        
display_board()
def check_if_win():
     if moves[6]== "X" or "Y":
          return
def check_if_tie():
    return

def check_if_game_over():
    check_if_win()
    check_if_tie()
check_if_game_over()

def flip_player():
    return
play_game()
    
    
