from random import randint

def new_board():
    """
    creates a blank board

    Returns:
        board: list with three list of spots on the board
    """
    return [[None, None, None], [None, None, None], [None, None, None]]

def render(boardvar):
    """
    renders the current version of the board

    Args:
        boardvar (list): prints the three lsit from the board argument
    """
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
    """
    gets the users input for a move

    Args:
        symbol (string): which user's move it is

    Returns:
        coordinates: returns a list of two coordinates on a board
    """
    y = input(f'{symbol}, What is your moves Y coordinate (Row):')
    x = input(f'{symbol}, What is your moves X coordinate (Column):')
    return [int(y)-1, int(x)-1]


def make_move(boardvar, coords, symbol):
    """
    excecutes a move, based on teh coordinates provided

    Args:
        boardvar (list): list with three list of spots on the board
        coords (list): a list of two coordinates on a board
        symbol (string): the symbol used by the current players move

    Returns:
        board: list with three list of spots on the board
    """
    boardvar[coords[0]][coords[1]] = symbol
    return boardvar


def validate_move(boardvar, coords):
    """
    checks if the coordinates provided for a move are valid. by checking the current open postitions against the coords argument
    
    Args:
        boardvar (list): list with three list of spots on the board
        coords (list): a list of two coordinates on a board

    Returns:
        _type_: _description_
    """
    if coords[0] < 3 and coords[0] > -1 and coords[1] < 3 and coords[1] > -1:
        if boardvar[coords[0]][coords[1]] is None:
            return True
        else:
            return False
    else:
        return False


def get_winner(boardvar, symbol):
    """
    checks if one of the win conditions has been met for the player

    Args:
        boardvar (list): list with three list of spots on the board
        symbol (string): the symbol used by the current players move

    Returns:
        bool: returns the result of the check
    """
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
    """
    checks if there is any move left to play

    Args:
        boardvar (list): list with three list of spots on the board

    Returns:
        bool: returns the result of the check
    """
    for row in boardvar:
        for item in row:
            if item is None:
                return True
    return False


def random_move():
    """
    generates a random move for the ai move

    Returns:
        _type_: _description_
    """
    move = [randint(0, 2), randint(0,2)]
    return move