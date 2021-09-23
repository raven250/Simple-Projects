import numpy as np

num_rows = 6
num_columns = 7

def who_won(turn):
    if turn%2 == 0:
        print("Player Two Wins!")
    else:
        print("Player One Wins!")

def check_board(board, turn):
    #Horizontal Check
    for c in range(num_columns - 3):
        for r in range(num_rows):
            if board[r,c] != 0 and board[r,c] == board[r,c+1] == board[r,c+2] == board[r,c+3]:
                return True

    #Vertical Check
    for c in range(num_columns):
        for r in range(num_rows - 3):
            if board[r,c] != 0 and board[r,c] == board[r+1,c] == board[r+2,c] == board[r+3,c]:
                return True

    #Left Diagonal Check
    for c in range(num_columns-3):
        for r in range(num_rows-3):
            if board[r,c] != 0 and board[r,c] == board[r+1,c+1] == board[r+2,c+2] == board[r+3,c+3]:
                return True

    #Right Diagonal Check
    for c in range(3, num_columns):
        for r in range(num_rows-3):
            if board[r,c] != 0 and board[r,c] == board[r+1,c-1] == board[r+2,c-2] == board[r+3,c-3]:
                return True

def create_board():
    board = np.zeros((num_rows, num_columns))
    return board

def player_move(turn, board):

    if turn%2 == 0:
        print("Player one turn, enter a column")
    elif turn%2 == 1:
        print("Player two turn, enter a column")
    move_one = input()

    try:
        val_one = int(move_one)
    except ValueError:
        print("That's not an int!")

    try:
        for i in range(num_rows-1, -1, -1):
            if board[i,val_one] == 0 and turn%2 == 0:
                board[i,val_one] = 1
                turn+=1
                break
            elif board[i,val_one] == 0 and turn%2 == 1:
                board[i,val_one] = 2
                turn+=1
                break

    except:
        print("Column out of range!")
    return turn, board

new_board = create_board()
print(new_board)
endgame = 0
turn = 0

while endgame < 1:
    turn, new_board = player_move(turn, new_board)
    print(new_board)
    if(check_board(new_board, turn)):
        who_won(turn)
        endgame += 1

print("End of Game")
