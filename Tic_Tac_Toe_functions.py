import random

import os

def clear():
    os.system( 'cls' )

def display_board(board):
    clear()
    print(board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('---------')
    print(board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3]+' ')

def player_input():
    
    marker = ''
    #keep asking player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        
        marker = input('Player 1 please choose either X or O: ')
        
    player1 = marker
    
    #assign player 2 the opposite marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return(player1,player2)

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    
    #check rows, columns, and diagonals
    
    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    
    #Board is full if we return True
    return True

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input('Choose a position (1-9): '))
        except ValueError:
            print('Please input a valid integer.')
            continue
        else:
            #valid input
            break        
    
    return position

def replay():
    
    choice = input('Play again? Please enter Yes or No: ')
    
    return choice == 'Yes' or  choice == 'yes'
