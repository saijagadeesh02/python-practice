#from Ipython.display import clear_output
#displaying the game_board
def display_board(board):
    print('\n'*25)
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
test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#marker selection

def player_input():
    marker = ''
    while(marker != 'X' and marker!= 'O'):
        marker=input('player1: Please pick a marker X or O ?').upper()
    if marker == 'X':
        return(['X','O'])
    else:
        return(['O','X'])

def marker_input(cp):
    if(cp == d[0]):
        pos = int(input('player1 : use the keypad to place the marker'))
        place_marker(cp,pos)
        if win_check():
            print("Player 1 has won the game! congos :)")
            display_board(test_board)
            return cp
        cp = d[1]
    else:
        pos = int(input('player2 : use the keypad to place the marker'))
        place_marker(cp,pos)
        if win_check():
            print("Player 2 has won the game! congos :)")
            display_board(test_board)
            return cp
        cp = d[0]
    display_board(test_board)
    return cp

def place_marker(marker,position):
    if (position < 10):
        test_board[position] = marker

def win_check():
    if ((test_board[1]==test_board[2]==test_board[3]==cp) or (test_board[4]==test_board[5]==test_board[6]==cp) or (test_board[7]==test_board[8]==test_board[9]==cp)):
        return True
    if ((test_board[1]==test_board[4]==test_board[7]==cp) or (test_board[2]==test_board[5]==test_board[8]==cp) or (test_board[3]==test_board[6]==test_board[9]==cp)):
        return True
    if ((test_board[1]==test_board[5]==test_board[9]==cp) or (test_board[3]==test_board[5]==test_board[7]==cp)):
        return True


def board_check():
    for i in range(1,10):
        flag = 0
        if test_board[i] == ' ':
            flag = 1
    if flag == 1:
        return True
    else:
        return False

d=player_input()
cp = d[0] #current player
while board_check():
    if not win_check():
        cp = marker_input(cp)
    else:
        break

#display_board(test_board)