

from random import randint


def new_board():
    return [[None, None, None], [None, None, None], [None, None, None]]

def render(boardvar):
    print('---')
    for row in boardvar:
        printlist = []
        for item in row:
            
            if item is None:
                printlist.append(' ')
            if item == 'X':
                printlist.append('X')
            if item == 'O':
                printlist.append('O')

        
        print(printlist[0], printlist[1], printlist[2])
    print('---')
        
def get_move(symbol):
    y = input(f'{symbol}, What is your moves Y coordinate (Row):')
    x = input(f'{symbol}, What is your moves X coordinate (Column):')
    return [int(y)-1, int(x)-1]

# print(get_move())

def make_move(boardvar, coords, symbol):
    boardvar[coords[0]][coords[1]] = symbol
    return boardvar


def validate_move(boardvar, coords):
    # if type(coords[0]) is not int or type(coords[1]) is not int:
    #     return False
    
    if coords[0] < 3 and coords[0] > -1 and coords[1] < 3 and coords[1] > -1:
        if boardvar[coords[0]][coords[1]] is None:
            return True
    else:
        return False


def get_winner(boardvar, symbol):
    for row in boardvar:
        if row == [symbol, symbol, symbol]:
            return True

    i = 0
    while i < 3:
        if boardvar[0][i] == symbol and boardvar[1][i] == symbol and boardvar[2][i] == symbol:
            return True
        else:
            i += 1

    if boardvar[0][0] == symbol and boardvar[1][1] == symbol and boardvar[2][2] == symbol:
        return True

    if boardvar[0][2] == symbol and boardvar[1][1] == symbol and boardvar[2][0] == symbol:
        return True

    else:
        return False

def any_move_left(boardvar):
    for row in boardvar:
        for item in row:
            if item is None:
                return True
    return False

def random_move():
    move = [randint(0,2), randint(0,2)]
    return move