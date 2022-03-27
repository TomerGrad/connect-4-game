"""
Here will be Dragons
"""
from random import randrange

def printboard(board):
    print("1 2 3 4 5 6 7")
    print("V V V V V V V")
    for row in board:
        print("|".join(row))
    print()

def turn(player, col, board):
    if board[0][col] != " ":
        raise KeyError
    for i, row in enumerate(reversed(board)):
        if row[col] == " ":
            row[col] = player
            return len(board) - 1 - i, col

def checkrow(board, lastturn, player):
    rowpos = lastturn[0]
    return player*4 in ''.join(board[rowpos])

def checkcol(board, lastturn, player):
    rowpos, colpos = lastturn
    return player*4 in ''.join([board[i][colpos] for i in range(rowpos, len(board))])

def checkdiag(board, lastturn, player):
    rowpos, colpos = lastturn
    posit_diag = neg_diag = board[rowpos][colpos]
    rightlim = colpos
    uplim = rowpos
    leftlim = len(board[rowpos]) - colpos
    bottomlim = len(board) - rowpos
    for i in range(1, min(uplim, rightlim)):
        posit_diag = board[rowpos-i][colpos-i] + posit_diag
    for j in range(1, min(leftlim, bottomlim)):
        posit_diag = posit_diag + board[rowpos+j][colpos+j]
    for i in range(1, min(uplim, leftlim)):
        neg_diag = board[rowpos-i][colpos+i] + neg_diag
    for j in range(1, min(bottomlim, rightlim)):
        neg_diag = neg_diag + board[rowpos+j][colpos-j]
    return (player*4 in posit_diag) or (player*4 in neg_diag)

def victory(board, lastturn: tuple, player):
    return any((checkcol(board, lastturn, player), checkrow(board, lastturn, player), checkdiag(board, lastturn, player)))

def create_board():
    return [[' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ']]

if __name__ == '__main__':
    board: list = [[' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' '],
                   [' ',' ',' ',' ',' ',' ',' ']]
    X = "X"
    O = "O"
    player = X
    isX = True
    lastturn = (0, 0)
    vi = victory(board, lastturn, player)

    while not vi:
        printboard(board)
        try:
            #if player == X:
            col = int(input("Choose column: ")) - 1
            lastturn = turn(player, col, board)
            #else:
            #    lastturn = turn(player, randrange(0, 6), board)
        except KeyError:
            continue
        except (IndexError, ValueError):
            print("Bad column try again")
            continue
        vi = victory(board, lastturn, player)
        if vi:
            print(f"{player} has Won!")
            printboard(board)
        isX = not isX
        player = (O, X)[isX]
