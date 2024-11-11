board = [["?","?","?"],["?","?","?"],["?","?","?"]]

def boardDisplay(board): # Displays the board in terminal
    print(board[0][0] + "|" + board[1][0] + "|" + board[2][0])
    print("—————")
    print(board[0][1] + "|" + board[1][1] + "|" + board[2][1])
    print("—————")
    print(board[0][2] + "|" + board[1][2] + "|" + board[2][2])

def boardUpdate(board, move_x, move_y, letter): # Adds move to board
    board[move_x][move_y] = letter
        

def checkWinner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "?": # Checks if three are in a row vertically
            return True
        elif board[0][i] == board[1][i] == board[2][i] != "?": # Check if three are in a row horizontally
            return True
        elif board[0][0] == board[1][1] == board[2][2] != "?": # Checks the top left to bottom right diagonal
            return True
        elif board[0][2] == board[1][1] == board[2][0] != "?"  : # Checks the bottom left to top right diagonal
            return True
        else:
            return False
            
def checkDraw(): # Checks if game ended in draw
    return not any("?" in subboard for subboard in board)



game = True

while game: # game loop
    if checkDraw():
        print("Draw.")
        game += False
        break
    
    boardDisplay(board)
    move_x1 = int(input("Player 1, enter your x coordinate:"))
    move_y1 = int(input("Player 1, enter your y coordinate:"))
    print("Player 1 made his move.")
    boardUpdate(board, move_x1, move_y1, "X")
    boardDisplay(board)
    if checkWinner():
        print("Player 1 won.")
        game += False
        break
    
    if checkDraw():
        print("Draw.")
        game += False
        break
    
    move_x2 = int(input("Player 2, enter your x coordinate:"))
    move_y2 = int(input("Player 2, enter your y coordinate:"))
    boardUpdate(board, move_x2, move_y2, "O")
    boardDisplay(board)
    if checkWinner():
        print("Player 2 won.")
        game += False
        break
    print("-------------------------------------------------------------")
    