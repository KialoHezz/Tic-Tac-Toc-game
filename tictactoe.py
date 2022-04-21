
'''
created the list called board
'''
# global variable- to run by default


game_ongoing = True

winner = None

player = "X"

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# display the board at the terminal
def display_board():
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8])
  


def play_game():
    display_board()


    while game_ongoing:
        handle_turn(player)

        check_game_over()

        flip_player()

    
    # games ends
    if winner == "X" or winner == "0":
        print(winner + " You  won")
    elif winner == None:
        print("Tie")

def handle_turn(player):
    position = input("Choose position from 1-9:")
    position = int(position) - 1


    board[position] = player
    display_board()


def check_game_over():
   
    check_if_win()

    check_if_tie()


def check_if_win():
# set up gloa
    global winner 
     # check row
    row_winner = check_row()
    # check column
    column_winner = check_column()
    # check diagonal
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner :
        winner = diagonal_winner
    else:
        winner = None


def check_if_tie():
    return    

def check_row():
    global game_ongoing

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_ongoing = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    
    return

def check_column():
    global game_ongoing

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_ongoing = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonal():

    global game_ongoing

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
   

    if diagonal_1 or diagonal_2 :
        game_ongoing = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    
    return    

def check_if_win():
    return

def check_if_tie():
    global game_ongoing

    if "-" not in board:
        game_ongoing=False
    return


def flip_player():
    global player

    if player == "X":
        player ="O"
    elif player == "O":
        player = "x"
    return

play_game()