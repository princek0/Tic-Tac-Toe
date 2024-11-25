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
    
    i = 0

    while i <= 2:
        if board[i][0] == board[i][1] == board[i][2] != "?": # Checks if three are in a row vertically
            return True
        elif board[0][i] == board[1][i] == board[2][i] != "?": # Check if three are in a row horizontally
            return True
        elif board[0][0] == board[1][1] == board[2][2] != "?": # Checks the top left to bottom right diagonal
            return True
        elif board[0][2] == board[1][1] == board[2][0] != "?"  : # Checks the bottom left to top right diagonal
            return True
        else:
            i += 1
    
    return False
            
def checkDraw(): # Checks if game ended in draw
    return not any("?" in subboard for subboard in board)



game = True # variable for game loop

print("The coordinates start at [0][0] at the top left square to [2][2] in the bottom right.")

while game: # game loop
    if checkDraw():
        print("Draw.")
        game += False
        break
    
    boardDisplay(board)

    while True: 
        try: 
            move_x1 = int(input("Player 1, enter your x coordinate:"))
            move_y1 = int(input("Player 1, enter your y coordinate:"))
            if not 0 <= move_x1 <= 2 or not 0<= move_y1 <= 2: # checks if user input is valid
                print("Enter integers between 0 and 2.")
            elif not board[move_x1][move_y1] == "?": # checks if selected square has been occupied
                print("That square is occupied. Retry.")
            else:
                break

        except ValueError:
            print("Enter integers between 0 and 2.")

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
    
    while True: 
        try: 
            move_x2 = int(input("Player 2, enter your x coordinate:"))
            move_y2 = int(input("Player 2, enter your y coordinate:"))
            if not 0 <= move_x2 <= 2 or not 0<= move_y2 <= 2:
                print("Enter integers between 0 and 2.")
            elif not board[move_x2][move_y2] == "?":
                print("That square is occupied. Retry.")
            else:
                break

        except ValueError:
            print("Enter integers between 0 and 2.")

    print("Player 2 made his move.")
    boardUpdate(board, move_x2, move_y2, "O")
    boardDisplay(board)
    if checkWinner():
        print("Player 2 won.")
        game += False
        break

    print("-------------------------------------------------------------")
    
