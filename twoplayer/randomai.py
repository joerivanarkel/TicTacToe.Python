from base import new_board, random_move, render, get_move, make_move, get_winner, any_move_left, validate_move

board = new_board()
game_ongoing = True
winner = None
draw = None

while game_ongoing is True:
        
    # X Moves
    result = False
    while result is False:
        move = get_move('X')
        result = validate_move(board, move)
        if result is True:
            board = make_move(board, move, 'X')
            result = False
            break
    
    
    render(board)
    
    winresultx = get_winner(board, 'X')
    if winresultx is True:
        game_ongoing = False
        winner = 'X'
        break
    
    drawresultx = any_move_left(board)
    if drawresultx is False:
        draw = True
        break
    
    # AI Moves
    aimove = random_move()
    board = make_move(board, aimove, 'O')
    render(board)

    winresulto = get_winner(board, 'O')
    if winresulto is True:
        game_ongoing = False
        winner = 'O'
        break

    drawresulto = any_move_left(board)
    if drawresulto is False:
        draw = True
        break


if winner == 'X':
    print('X Has Won')
    
if winner == 'O':
    print('O has won') 

if draw is True:
    print('It is a draw')