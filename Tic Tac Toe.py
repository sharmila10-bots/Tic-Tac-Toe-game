#Tic tac toe game code in python
#Creating board for display
board=["*","*","*",
       "*","*","*",
       "*","*","*"]

#making starting player as X
current_player="X"
winner=None
game_is_going=True

#function to display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-","-","-","-","-")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-", "-", "-", "-", "-")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("-", "-", "-", "-", "-")

#function to swap from X to O
def handle_turn():
    global count
    print("Now it's {} turn".format(current_player))
    position=int(input("Enter the position from 0 to 8:"))
    if board[position]=="*":
        board[position]=current_player
    else:
        print("Position is filled...enter other position")
        handle_turn()
    display_board()

#main function
def play_game():
    global game_is_going
    display_board()
    while game_is_going:
        handle_turn()

        flip_player()

        check_if_winner()

    #condition to check for winner
    if winner=="X" or winner=="O":
        print("Game Over !")
        print("winner is",winner)
    else:
        print("Game Over !")
        print(" Game is on Tie")

#function to generate winner
def check_if_winner():
    global winner
    row_winner=check_row()
    col_winner=check_col()
    dia_winner=check_dia()
    tie=check_tie()


    if row_winner:
       winner=row_winner
    elif col_winner:
        winner=col_winner
    elif dia_winner:
        winner=dia_winner
    elif tie:
        winner = tie

#function to check for row condition
def check_row():
    global game_is_going
    row_1 = board[0] == board[1] == board[2] != "*"
    row_2 = board[3] == board[4] == board[5] != "*"
    row_3 = board[6] == board[7] == board[8] != "*"
    if row_1 or row_2 or row_3:
        game_is_going=False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

#function to check for column condition
def check_col():
    global game_is_going
    col_1 = board[0] == board[3] == board[6] != "*"
    col_2 = board[1] == board[4] == board[7] != "*"
    col_3 = board[2] == board[5] == board[8] != "*"
    if col_1 or col_2 or col_3:
        game_is_going = False

    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]

#function to check for diagonal condition
def check_dia():
    global game_is_going
    dia_1 = board[0] == board[4] == board[8] != "*"
    dia_2 = board[2] == board[4] == board[6] != "*"

    if dia_1 or dia_2:
        game_is_going = False

    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]


#funtion to define the swap of the player
def flip_player():
    global current_player

    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"

#function to check whether game is tie
def check_tie():
    global game_is_going
    if(board[0]!="*" and board[1]!="*" and board[2]!="*" and board[3]!="*" and board[4]!="*" and board[5]!="*" and board[6]!="*" and board[7]!="*" and board[8]!="*"):
        game_is_going = False
        return 1

#call for game function
play_game()

