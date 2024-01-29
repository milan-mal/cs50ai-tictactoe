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
    raise NotImplementedError


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
