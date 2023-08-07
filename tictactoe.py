# a fun little tic tac to game in Python

import random

board = [' ' for x in range(10)]

def insert_letter(letter, pos):
    board[pos] = letter

def space_is_free(pos):
    return board[pos] == ' '

def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# must use the \ to indicate that the statement is continued on the next line (unble to just press enter)

def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
    (bo[4] == le and bo[5] == le and bo[6] == le) or \
    (bo[1] == le and bo[2] == le and bo[3] == le) or \
    (bo[1] == le and bo[4] == le and bo[7] == le) or \
    (bo[2] == le and bo[5] == le and bo[8] == le) or \
    (bo[3] == le and bo[6] == le and bo[9] == le) or \
    (bo[1] == le and bo[5] == le and bo[9] == le) or \
    (bo[3] == le and bo[5] == le and bo[7] == le)

def player_move():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('The space you selected is occupied. Please select a free space.')
            else:
                print('Please type a number between 1 and 9!')
        except:
            print('Please follow the instructions and choose a number between 1 and 9.')

def comp_move():
    possible_moves = [x for x,letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[1] = let
            if is_winner(board_copy, let):
                move = i
                return move
    
    corners_open = []
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move
    
    if 5 in possible_moves:
        move = 5
        return move
    
    edges_open = []
    for i in possible_moves:
        if i in [2,4,6,8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)
    
    return move

def select_random(li):
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe, Player!')
    print_board(board)

    while not(is_board_full(board)):
        if not(is_winner(board,'O')):
            player_move()
            print_board(board)
        else:
            print("LOL, the computer beat you!")
            break
        
        if not(is_winner(board,'X')):
            move = comp_move()
            if move == 0:
                print("lol, you tied a computer in tic tac toe!")
            else:
                insert_letter('O', move)
                print("Computer placed an 'O' in position", move, ":")
                print_board(board)
        else:
            print("Oh jees wow you beat the computer in tic tac toe!")
            break

    if is_board_full(board):
        print('The game is over.')

main()
