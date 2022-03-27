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
    
def create_ships():
    '''
    Random hidden ships for user to find
    '''
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)

def get_ship_loction():
    '''
    Ask user what row and column they want to choose to find the ship
    '''
    pass

def count_hit_ships():
    '''
    Count every time the user hits a ship. 
    When you hit all 5 the game is over.
    '''
    pass   

create_ships()
turn = 10
# while turns > 0: