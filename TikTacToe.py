board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))

# This functions is for each player turn
def turn(player):
    TurnOK = False
    # Get input of a row an column and check that the input is valid
    while TurnOK == False:
        row = int(input(f"Player {player} - Select a row:"))
        column = int(input(f"Player {player} - Select a column:"))
        if(row in [0, 1, 2] and column in [0, 1, 2] and board[row][column] == '_'):
            board[row][column] = player
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
            TurnOK = True
        else:
            print("Please select numbers between 0-2, and a free space")
        checkWin(player)
        IsboardFull()
        continue

# This function checks for a winner
def checkWin(player):
    # Checks for a row win (X,X,X or O,O,O)
    for r in range(3):
        if(board[r] == [player,player,player]):
            print(f"{player} Won")
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
            exit()

    # Checks for a column win (X    O
    #                          X or O
    #                          X    O)
    for c in range(3):
        if(board[0][c] == player and board[1][c] == player and board[2][c] == player):
            print(f"{player} Won!!!")
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
            PlayAgain = input("Would you like to play again? (Y/N)")
            if PlayAgain == "Y":
                startGame()
            else:
                exit()

    # Checks for a diagonal win (X          O
    #                               X   or     O
    #                                  X          O)
    if(board[0][0] == player and board[1][1] == player and board[2][2] == player):
        print(f"{player} Won!!!")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
        PlayAgain = input("Would you like to play again? (Y/N)")
        if PlayAgain == "Y":
            startGame()
        else:
            exit()
    elif(board[0][2] == player and board[1][1] == player and board[2][0] == player):
        print(f"{player} Won!!!")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
        PlayAgain = input("Would you like to play again? (Y/N)")
        if PlayAgain == "Y":
            startGame()
        else:
            exit()

def IsboardFull():
    result = '_' in (item for sublist in board for item in sublist)
    if result != True:
        print("It's a tie!")
        PlayAgain = input("Would you like to play again? (Y/N)")
        if PlayAgain == "Y":
            startGame()
        else:
            exit()
def startGame():
    board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    for i in range(5):
        play()

def play():
    turn("X")
    turn("O")

startGame()

