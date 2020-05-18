# Tic-tac-toe
#displaying the game_board
def display_board(board):
    print('\n'*15)
    #clear_output()
    print('  |   |')
    print(board[7] +' | '+board[8]+' | '+board[9])
    print('---------')
    print('  |   |')
    print(board[4] +' | '+board[5]+' | '+board[6])
    print('---------')
    print('  |   |')
    print(board[1] +' | '+board[2]+' | '+board[3])
    print('\n'*3)
#test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#display_board(test_board)


def player_input():
    marker = ''
    while(marker != 'X' and marker!= 'O'):
        marker=input('player1: Please pick a marker X or O ?').upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board, mark):
    if ((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark)):
        return True
    if ((board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark)):
        return True
    if ((board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark)):
        return True

# def choose_first():
#     flip = random.randint(0,1)
#     if flip == 0:
#         return 'Player 1'
#     else:
#         return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    return True #Board is Full

def player_choice(board):
    position = 0

    while position not in range(1,10) or not space_check(board,position):
        position = int(input('choose a position: (1-9)'))
    return position
def  replay():

    choice = input("Play again ? Enter Yes or No").lower()
    return choice == 'yes'

# Main loop for the game

print("Welcome to tic tac toe")
while True:
    turn = 'Player 1' #choose first
    the_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_mark,player2_mark=player_input()
    game_on = True
    while game_on:

        if turn == 'Player 1':

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_mark,position)
            if win_check(the_board,player1_mark):
                display_board(the_board)
                print("Player 1 has won the game")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_mark,position)
            if win_check(the_board,player2_mark):
                display_board(the_board)
                print("Player 2 has won the game")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie")
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break
