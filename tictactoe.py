"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def stateXWinnerRow():
    return [[X, X, X],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def stateOWinnerRow():
    return [[EMPTY, EMPTY, EMPTY],
            [O, O, O],
            [EMPTY, EMPTY, EMPTY]]

def stateNoWinnerRandom():
    return [[EMPTY, X, EMPTY],
            [O, X, O],
            [EMPTY, O, EMPTY]]

def stateXWinnerDiag():
    return [[X, X, EMPTY],
            [O, X, O],
            [EMPTY, O, X]]

def stateOWinnerDiag():
    return [[X, X, O],
            [X, O, EMPTY],
            [O, O, X]]

    # return [[X, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]

    # return [[EMPTY, O, EMPTY],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]

    # return [[EMPTY, EMPTY, EMPTY],
    #         [X, O, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    xCount = 0
    oCount = 0

    for i in board:
        xCount += i.count(X)
        oCount += i.count(O)

    if xCount > oCount:
        print('O\'s turn')
        return O
    else:
        print('X\'s turn')
        return X

# player(initial_state())


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] is EMPTY:
                possibleActions.add((row, col))
    
    print('possibleActions', possibleActions)
    return possibleActions

# actions(initial_state())


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = X

    print('newBoard', newBoard)
    return newBoard

# result(initial_state(), actions(initial_state()).pop())


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check rows/cols for a winner
    def checkBoard(inputBoard):
        for i in board:
            xCount = 0
            oCount = 0
            xCount += i.count(X)
            oCount += i.count(O)
            if xCount == 3:
                return X
            elif oCount == 3:
                return O
        return None
    
    # check rows for a winner
    winner = checkBoard(board)

    # check columns for a winner
    if winner is None:
        boardInverted = copy.deepcopy(board)
        for row in range(3):
            for col in range(3):
                boardInverted[col][row] = board[row][col]

        winner = checkBoard(boardInverted)

    # check columns for a winner
    middle = board[1][1]
    if middle is not None:
        if board[0][0] == middle and board[2][2] == middle:
            winner = middle
        elif  board[0][2] == middle and board[2][0] == middle:
            winner = middle

    print('winner:', winner)
    return winner

print('--- check winner for initial_state ---')
winner(initial_state())
print('--- check winner for stateXWinnerRow ---')
winner(stateXWinnerRow())
print('--- check winner for stateOWinnerRow ---')
winner(stateOWinnerRow())
print('--- check winner for stateNoWinnerRandom ---')
winner(stateNoWinnerRandom())
print('--- check winner for stateXWinnerDiag ---')
winner(stateXWinnerDiag())
print('--- check winner for stateOWinnerDiag ---')
winner(stateOWinnerDiag())


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # TODO
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
