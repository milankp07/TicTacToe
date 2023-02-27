#!/usr/bin/env python
# coding: utf-8

# DISPLAY BOARD 
# TAKE PLAYER INPUT
# PLACE THEIR INPUT ON THE BOARD
# CHECK IF GAME IS WON TIED LOST OR ONGOING
# REPEAT C & D UNTIL THE GAME HAS BEEN WON OR TIED
# ASK IF PLAYERS WANT TO PLAY AGAIN

my_board = [' ']*10

# DISPLAY BOARD
def display_board(board):
    print(f"{board[1]}  | {board[2]} |  {board[3]}")
    print("-----------")
    print(f"{board[4]}  | {board[5]} |  {board[6]}")
    print("-----------")
    print(f"{board[7]}  | {board[8]} |  {board[9]}")

# display_board(my_board)

# IF SPACE IS TAKEN OR NOT
def space_check(board,index):
    if board[index] != ' ':
        return True
    else:
        return False

# PLAYER INPUT
def player_input(board):
    flag=True    
    while flag:
        input_number = input('Enter number in between 1 to 9 : ')
        if input_number.isdigit():
            if int(input_number) in range(1,10):
                if space_check(board,int(input_number)) == False:
                    return int(input_number)
                    flag=False
                else:
                    print('Space is taken.')
                    flag=True
            else :
                print('Exceeded range. Range is 1 to 9.')
                flag= True
        else :
            print('No entered is not valid. Enter again.')

            
# PLAYER SYMBOL SELECTION
def player_symbol():
    flag=True
    while flag :
        input_symbol = input('Enter the symbol "X" or "O" : ')
        if input_symbol in ['X','O'] :
            return input_symbol
        else :
            print('Invalid selection. Enter again.')

# MODIFY BOARD BASED ON PLAYER INPUT
def modify_board(board,symbol,number):
    board[number] = symbol 
    return board

# IF GAME IS WON 
def win_game_check(board,symbol):
    if symbol=='X':
        if (board[1]==board[2]==board[3]=='X') or (board[3]==board[6]==board[9]=='X') or (board[9]==board[8]==board[7]=='X') or (board[7]==board[4]==board[1]=='X') or (board[1]==board[5]==board[9]=='X') or (board[3]==board[5]==board[7]=='X') :
            return True
    if symbol=='O':
        if (board[1]==board[2]==board[3]=='O') or (board[3]==board[6]==board[9]=='O') or (board[9]==board[8]==board[7]=='O') or (board[7]==board[4]==board[1]=='O') or (board[1]==board[5]==board[9]=='O') or (board[3]==board[5]==board[7]=='O'):
            return True

# IF GAME IS TIED
def tie_check(board):
    if ' ' in (board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9]):
        return False 
    else :
        return True

# PLAY AGAIN
def play_again():
    flag=True
    while flag:
        player_input=input('Do you want to play again? y for Yes or n for No? ')
        if player_input in ['y','n']:
            if player_input=='y':
                flag=False
                return True
            elif player_input=='n':
                flag=False
                return False
        else :
            print('Invalid choice. Enter again.')
            flag=True

# TIC TAC TOE GAME

while True:
    
    print('Welcome to the Tic-Tac-Toe game.')
    
    print('\n')

    board=[' ']*10

    display_board(board)
    print('\n')
    
    # WANT TO PLAY?
    want_to_play=input('Head into the game? y for Yes n for No? ')
    
    if want_to_play=='y':
        
        # SYMBOL SELECTION
        symbol = player_symbol()

        if symbol == 'X':
            print('Player 1 is "X" and Player 2 is "O"')
            player1_symbol = 'X'
            player2_symbol = 'O'
        elif symbol == 'O':
            player1_symbol = 'O'
            player2_symbol = 'X'
            print('Player 1 is "O" and Player 2 is "X"')
        
        # DEFAULT TURN
        turn= "Player 1"
        
        # GAME ON FLAG
        game_on = True
        
    else :
        
        break     

    while game_on :
        
        # PLAYER 1 TURN
        if turn == "Player 1":  
            print('\n')
            print(f'Player 1 turn. Your symbol is {player1_symbol}.')
            input_number = player_input(board)
            modify_board(board,player1_symbol,input_number)
            print('\n')
            display_board(board)
            turn = "Player 2"
            game_on=True
            # CHECK IF PLAYER 1 WON
            if win_game_check(board,player1_symbol):
                print('\n')
                print('Player 1 wins.')
                game_on=False
                break
            # CHECK IF ITS A TIE
            if tie_check(board)==True:
                print('\n')
                print('Tied')
                game_on=False
                break

        # PLAYER 2 TURN
        if turn == "Player 2":
            print('\n')
            print(f'Player 2 turn. Your symbol is {player2_symbol}.')
            input_number = player_input(board)
            modify_board(board,player2_symbol,input_number)
            print('\n')
            display_board(board)
            turn = "Player 1"
            game_on=True
            # CHECK IF PLAYER 2 WON
            if win_game_check(board,player2_symbol):
                print('\n')
                print('Player 2 wins.')
                game_on=False
                break
            # CHECK IF ITS A TIE
            if tie_check(board)==True:
                print('\n')
                print('Tied')
                game_on=False
                break
                
    # DO YOU WANT TO PLAY AGAIN?
    if play_again()==False:
        break
