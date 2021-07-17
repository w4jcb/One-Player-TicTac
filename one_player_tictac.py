import os
import time
import string
from random import *

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen  => cls()

#line = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def Display_board(board):
    # Displayes the empty board before input and displayes values on board  after input by users
    cls()
    print("\t\t\t    |   | ")
    print("\t\t\t ",board[1],"|",board[2], "|",board[3],"")
    print("\t\t\t    |   | ")
    print("\t\t\t-------------")
    print("\t\t\t    |   | ")
    print("\t\t\t ",board[4],"|",board[5], "|",board[6],"")
    print("\t\t\t    |   | ")
    print("\t\t\t------------")
    print("\t\t\t    |   | ")
    print("\t\t\t ",board[7],"|",board[8], "|",board[9],"")
    print("\t\t\t    |   | ")
    print("\n\n\n")# spaces for board separation 


def input_player():
    name1=input("Please enter your name: ")
    name2=('The Computer')
    pl={"X":name1,"O":name2} # assigning person X and computer O
    return pl

    

def position_board(position,board,player):
    # places  input value to a position in list .here name of list is board
    board[position] = player

def winner_check(board,player):
    '''checks for winner using the conditions of tic tac toe'''
    return (board[1] == board[2] == board[3] == player or
            board[4] == board[5] == board[6] == player or
            board[7] == board[8] == board[9] == player or
            board[1] == board[4] == board[7] == player or
            board[2] == board[5] == board[8] == player or
            board[3] == board[6] == board[9] == player or
            board[1] == board[5] == board[9] == player or
            board[7] == board[5] == board[3] == player)


def go_first():
    # uses a random function to choose which player goes first
    import random
    if random.randint(1, 2) == 1:
        return "X"
    else:
        return "O"

def position_Check(board,position):
    # Boolean function:checks whether the position is availiable or not
    if board[position] == " ":
        return True
    else:
        return False

def board_Full(board,position_Check):
    # Boolean function:checks if the board is full
    for num in range(1,10):
        if position_Check(board,num):
            return False
    else:
        return True

def player_Input(board,player):
    # inputs position from users and validates whether the position is empty or not using position_check function
    choice = " "
    while((choice not in "1 2 3 4 5 6 7 8 9".split() or not  position_Check(board,int(choice)))):
        choice = input("{a}  what position do you want to choose from 1-9?".format(a=player))
    return int(choice)


def get_computer_move_smart(board,player):
    #print ("get_computer_move_smart - Checking for the WIN")
    choice = " "
    if board[1] == board[2] == player and board[3] ==" ": # 1-2-3
        choice = "3"
    elif board[1] == board[3] == player and board[2] ==" ": # 1-3-2
        choice = "2"
    elif board[2] == board[3] == player and board[1] ==" ": # 2-3-1
        choice = "1"

    elif board[4] == board[5] == player and board[6] ==" ": # 4-5-6
        choice = "6"
    elif board[4] == board[6] == player and board[5] ==" ": # 4-6-5
        choice = "5"
    elif board[5] == board[6] == player and board[4] ==" ": # 5-6-4
        choice = "4"
        
    elif board[7] == board[8] == player and board[9] ==" ": # 7-8-9
        choice = "9"
    elif board[7] == board[9] == player and board[8] ==" ": # 7-9-8
        choice = "8"
    elif board[8] == board[9] == player and board[7] ==" ": # 8-9-7
        choice = "7"

    elif board[1] == board[4] == player and board[7] ==" ": # 1-4-7
        choice = "7"
    elif board[1] == board[7] == player and board[4] ==" ": # 1-7-4
        choice = "4"
    elif board[4] == board[7] == player and board[1] ==" ": # 4-7-1
        choice = "1"

    elif board[2] == board[5] == player and board[8] ==" ": # 2-5-8
        choice = "8"
    elif board[2] == board[8] == player and board[5] ==" ": # 2-8-5
        choice = "5"
    elif board[5] == board[8] == player and board[2] ==" ": # 5-8-2
        choice = "2"

    elif board[3] == board[6] == player and board[9] ==" ": # 3-6-9
        choice = "9"
    elif board[3] == board[9] == player and board[6] ==" ": # 3-9-6
        choice = "6"
    elif board[6] == board[9] == player and board[3] ==" ": # 6-9-3
        choice = "3"

    elif board[1] == board[5] == player and board[9] ==" ": # 1-5-9
        choice = "9"
    elif board[1] == board[9] == player and board[5] ==" ": # 1-9-5
        choice = "5"
    elif board[5] == board[9] == player and board[1] ==" ": # 5-9-1
        choice = "1"

    elif board[3] == board[5] == player and board[7] ==" ": # 3-5-7
        choice = "7"
    elif board[3] == board[7] == player and board[5] ==" ": # 3-7-5
        choice = "5"
    elif board[5] == board[7] == player and board[3] ==" ": # 5-7-3
        choice = "3"

    else:
        choice = get_computer_move_ai(board)
        
    return int(choice)


def get_computer_move_ai(board):
    #print ("get_computer_move_ai - computer picking a move")
    # Check computer win moves
    for i in range(1, 10):
        if board[i] == ' ' and test_win_move(board, 'X', i):
            return i
    # Check player win moves
    for i in range(1, 10):
        if board[i] == ' ' and test_win_move(board, '0', i):
            return i
    # Check computer fork opportunities
    for i in range(1, 10):
        if board[i] == ' ' and test_fork_move(board, 'X', i):
            return i
    #  Check player fork opportunities
    for i in range(1, 10):
        if board[i] == ' ' and test_fork_move(board, '0', i):
            return i
    # Play a corner
    for i in [1, 3, 7, 9]:
        if board[i] == ' ':
            return i
    # Play center
    if board[5] == ' ':
        return 5
    #Play a side
    for i in [2, 4, 6, 8]:
        if board[i] == ' ':
            return i

def get_board_copy(board):
    # Make a duplicate of the board. When testing moves we don't want to 
    # change the actual board
    dupe_board = []
    for j in board:
        dupe_board.append(j)
    return dupe_board

def test_win_move(board, player, i):
    # player = 0 or X
    # i = the square to check if makes a win 
    b_copy = get_board_copy(board)
    b_copy[i] = player
    return winner_check(board,player)

def test_fork_move(board, player, i):
    # Determines if a move opens up a fork
    b_copy = get_board_copy(board)
    b_copy[i] = player
    winning_moves = 1
    for j in range(1, 10):
        if test_win_move(b_copy, player, j) and b_copy[j] == ' ':
            winning_moves += 1
    return winning_moves >= 2


def replay():
    # boolean function:asks users for replay.for Y.... input returns True otherwise returns false
    decision = input("Do you want to play again????").lower()
    if decision[0] == 'y':
        return True



Playing = True
while Playing:
    # main function for game.runs untill a the loop is exited using break
    os.system('clear') # for Linux
    os.system('cls') # for windows
    print('        \t                   Welcome To                           ')
    print('          \t                TIC     TAC     TOE                           \n')
    time.sleep(.4)
    board=[' ']*10
    print('\t\t\t\t   _1|_2_|_3__')
    print('\t\t\t\t   _4|_5_|_6_')
    print('\t\t\t\t    7| 8 | 9 \n')
    name=input_player() # asked for players name
    turn = go_first() #Picks who goes first
    time.sleep(1)
    print("\n\n")# spaces
    print("{a} will go first".format(a=name[turn]))
    time.sleep(1)
    game_on=True
    time.sleep(1)
    while game_on:
        if turn== "X":
            #player 1 Humand playing
            Display_board(board)
            status_fullboard = board_Full(board,position_Check)
            if winner_check(board, "O"):
                                game_on = False
                                print("Congrats {a} is the winner".format(a=name["O"]))
                                continue #break
            if status_fullboard:
                                game_on = False
                                print("Oops! It's a tie")
                                continue #break
            position=player_Input(board,name["X"])
            status_position = position_Check(board,position)
            if status_position == True:
                position_board(position, board, "X")
            
            turn="O"

            
        else:
            #player2 - computer playing
            Display_board(board)
            status_fullboard = board_Full(board,position_Check)
            if winner_check(board, "X"):
                                game_on = False
                                print("Congrats {a} is the winner".format(a=name["X"]))
                                continue #break
            if status_fullboard:
                                game_on = False
                                print("Oops! It's a tie")
                                continue #break
            position=get_computer_move_smart(board,"O")
            status_position = position_Check(board,position)
            if status_position == True:
                position_board(position, board, "O")
                #print(board)
        
            turn="X"
    if replay():
        continue
    else:
        print("Thank You for playing Tic Tac Toe\n bye bye bye")
        time.sleep(.7)
        Playing = False
