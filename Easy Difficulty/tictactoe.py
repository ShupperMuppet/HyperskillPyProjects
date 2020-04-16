r = [" ", " ", " "]
board = [r, r, r]
pawn = ["X", "O"]


def print_board():
    print("---------")
    for row in board:
        print("|", end=" ")
        for move in row:
            print(move, end=" ")
        print("|")
    print("---------")


def update_board(xval, yval, character):
    row = board[xval].copy()
    row[yval] = character
    board[xval] = row


print_board()
count = 9
while count > 0:
    # X moves first and O moves second
    x = 0
    y = 0
    whose_turn = 0
    try:
        y, x = input("Enter the coordinates: ").split()
        x = int(x)
        y = int(y)
        x = 3 - x
        y = y - 1
    except ValueError:
        print("You should enter numbers!")
        continue
    valid = [0, 1, 2]
    if (x not in valid) or (y not in valid):
        print("Coordinates should be from 1 to 3!")
    elif board[x][y] == ' ':
        whose_turn = (count + 1) % 2
        update_board(x, y, pawn[whose_turn])
        count -= 1
        print_board()
    else:
        print("This cell is occupied! Choose another one!")

    # Debug
    #board = [["O", "X", "O"], ["X", "O", "X"], ["X", "X", "O"]]

    # Win Conditions
    h1 = (board[0][0] == board[0][1] == board[0][2] == "X") or (board[0][0] == board[0][1] == board[0][2] == "O")
    h2 = (board[1][0] == board[1][1] == board[1][2] == "X") or (board[1][0] == board[1][1] == board[1][2] == "O")
    h3 = (board[2][0] == board[2][1] == board[2][2] == "X") or (board[2][0] == board[2][1] == board[2][2] == "O")
    v1 = (board[0][0] == board[1][0] == board[2][0] == "X") or (board[0][0] == board[1][0] == board[2][0] == "O")
    v2 = (board[0][1] == board[1][1] == board[2][1] == "X") or (board[0][1] == board[1][1] == board[2][1] == "O")
    v3 = (board[0][2] == board[1][2] == board[2][2] == "X") or (board[0][2] == board[1][2] == board[2][2] == "O")
    x1 = (board[0][0] == board[1][1] == board[2][2] == "X") or (board[0][0] == board[1][1] == board[2][2] == "O")
    x2 = (board[0][2] == board[1][1] == board[2][0] == "X") or (board[0][2] == board[1][1] == board[2][0] == "O")
    conditions = [h1, h2, h3, v1, v2, v3, x1, x2]
    print(conditions)

    # Win checking
    if h1 or h2 or h3 or v1 or v2 or v3 or x1 or x2:
        win = pawn[whose_turn]
        print(f"{win} wins")
        exit(0)

print("Draw")
