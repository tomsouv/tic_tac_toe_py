# Tic Tac Toe
# Tom S.
# 09/15/2021
# I attempted to create a functioning
# Tic Tac Toe game using Python
# based purely on my memory and
# knowledge of working Python so far.
# This is a project of mine for learning
# and developmental purposes as I pursue
# my learning of computer science and
# software engineering.

import random

def game():
    game_board = ['-','-','-','-','-','-','-','-','-']
    print('Welcome to Tic Tac Toe!')
    print('You will be X. The CPU will be O.') # I always choose X
    print('Enter the number that corresponds to the position you wish to add X to.')
    print('1' + ' | ' + '2' + ' | ' + '3')
    print('4' + ' | ' + '5' + ' | ' + '6')
    print('7' + ' | ' + '8' + ' | ' + '9')
    print('Here is the board: ')
    print(game_board[0] + ' | ' + game_board[1] + ' | ' + game_board[2] + '\n' + 
    game_board[3] + ' | ' + game_board[4] + ' | ' + game_board[5] + '\n' + 
    game_board[6] + ' | ' + game_board[7] + ' | ' + game_board[8])

    def game_win_check():
        # horizontal X win check
        if game_board[0] == 'X' and game_board[1] == 'X' and game_board[2] == 'X':
            print('You win!')
            # TS
            quit()
        elif game_board[3] == 'X' and game_board[4] == 'X' and game_board[5] == 'X':
            print('You win!')
            quit()
        elif game_board[6] == 'X' and game_board[7] == 'X' and game_board[8] == 'X':
            print('You win!')
            quit()
        # vertical X win check
        elif game_board[0] == 'X' and game_board[3] == 'X' and game_board[6] == 'X':
            print('You win!')
            quit()
        elif game_board[1] == 'X' and game_board[4] == 'X' and game_board[7] == 'X':
            print('You win!')
            quit()
        elif game_board[2] == 'X' and game_board[5] == 'X' and game_board[8] == 'X':
            print('You win!')
            quit()
        # diagonal X win check
        elif game_board[0] == 'X' and game_board[4] == 'X' and game_board[8] == 'X':
            print('You win!')
            quit()
        elif game_board[2] == 'X' and game_board[4] == 'X' and game_board[6] == 'X':
            print('You win!')
            quit()

        # horizontal O win check
        if game_board[0] == 'O' and game_board[1] == 'O' and game_board[2] == 'O':
            print('CPU wins!')
            quit()
        elif game_board[3] == 'O' and game_board[4] == 'O' and game_board[5] == 'O':
            print('CPU wins!')
            # TS
            quit()
        elif game_board[6] == 'O' and game_board[7] == 'O' and game_board[8] == 'O':
            print('CPU wins!')
            quit()
        # vertical O win check
        elif game_board[0] == 'O' and game_board[3] == 'O' and game_board[6] == 'O':
            print('CPU wins!')
            quit()
        elif game_board[1] == 'O' and game_board[4] == 'O' and game_board[7] == 'O':
            print('CPU wins!')
            quit()
        elif game_board[2] == 'O' and game_board[5] == 'O' and game_board[8] == 'O':
            print('CPU wins!')
            quit()
        # diagonal O win check
        elif game_board[0] == 'O' and game_board[4] == 'O' and game_board[8] == 'O':
            print('CPU wins!')
            quit()
        elif game_board[2] == 'O' and game_board[4] == 'O' and game_board[6] == 'O':
            print('CPU wins!')
            quit()
        else:
            return

    def cpu_logic():
        cpu_choice = random.randint(0,8)
        if '-' in game_board:
            if game_board[cpu_choice] == '-':
                game_board[cpu_choice] = 'O'
                return
            else:
                cpu_logic()
        else:
            print('No winner declared. Tie game.')
            quit()

    def game_logic():
        game_win_check()
        prompt = print('Select a number: ')
        user_choice = int(input())
        if '-' in game_board:
            if user_choice in range(1,10):
                if game_board[(user_choice - 1)] == '-':
                    game_board[(user_choice - 1)] = 'X'
                else:
                    print('Position is already taken, try again.')
                    game_logic()
            cpu_logic()
            print(game_board[0] + ' | ' + game_board[1] + ' | ' + game_board[2] + '\n' + 
                game_board[3] + ' | ' + game_board[4] + ' | ' + game_board[5] + '\n' + 
                game_board[6] + ' | ' + game_board[7] + ' | ' + game_board[8])
            game_logic()
        else:
            print('No winner declared. Tie game')
            quit()
            # TS
    game_logic()
game()


# win conditions:
#
# horizontally:
# 1-2-3
# 4-5-6
# 7-8-9
#
# vertically:
# 1-4-7
# 2-5-8
# 3-6-9
#
# diagonally:
# 1-5-9
# 3-5-7
