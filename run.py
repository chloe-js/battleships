# Legend
# X is for placing a ship and a hit battleship 
# ' ' is for available space
# '-' is for a missed shot

from random import randint


HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A':0, 'B':1, 'C':2,'D':3, 'E':4, 'F':5,'G':6, 'H':7}

def print_board(board):
    '''
    Create board to see where user can guess where to hit
    '''
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    
def create_ships(board):
    '''
    Random hidden ships for user to find
    '''
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'

def get_ship_loction():
    '''
    Ask user what row and column they want to choose to find the ship
    '''
    row = input('Enter ship row 1-8')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Enter ship row 1-8')
    column = input('Enter ship column A-H').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Enter ship column A-H').upper()
    return int(row) - 1, letters_to_numbers[column]

# user can still input no andswer and it will accept nothing as a turn if entered

def count_hit_ships(board):
    '''
    Count every time the user hits a ship. 
    When you hit all 5 the game is over.
    '''
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(HIDDEN_BOARD)
turn = 10
while turns > 0:
    print('WELCOME TO BATTLESHIP')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print('You already guessed that')
    elif HIDDEN_BOARD[row][column] == 'X':
        print('DIRECT HIT! you sunk a battleship')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1