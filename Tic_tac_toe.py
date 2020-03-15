from Tic_Tac_Toe_Functions import functions

import random

import os

print('Welcome to Tic Tac Toe. Created by yan')

while True:
    
    #assign marker
    board = [' ']*10
    player1_marker, player2_marker = functions.player_input()
    
    #who goes first
    turn = functions.choose_first()
    print(turn + ' will go first')
    
    #ready to play?
    play_game = input('Ready to play? y or n: ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    #Game play
    while game_on:
        
        #player 1 turn
        if turn == 'Player 1':
            functions.display_board(board)
            #choose position
            position = functions.player_choice(board)
            #place marker on position
            functions.place_marker(board, player1_marker, position)
            #check if they won
            if functions.win_check(board, player1_marker):
                functions.display_board(board)
                print('Player 1 has won!')
                game_on = False
            else:
            #check if tie
                if functions.full_board_check(board):
                    functions.display_board(board)
                    print('Tie game!')
                    game_on = False
             #no tie and no win. Then next players turn
                else:
                    turn = 'Player 2'
        
        else:
            functions.display_board(board)
            
            position = functions.player_choice(board)
            
            functions.place_marker(board, player2_marker, position)
            
            if functions.win_check(board, player2_marker):
                functions.display_board(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if functions.full_board_check(board):
                    functions.display_board(board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 1'
                    
    if not functions.replay():
        break
        
