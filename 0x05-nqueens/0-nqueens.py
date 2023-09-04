#!/usr/bin/python3
"""Module that solves the N queens problem
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the
    given position (row, col) on the board.

    Args:
        board (list): The current state of the board.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.

    Returns:
        bool: True if it's safe to place a queen
        at the given position, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def nqueens_util(board, row, result):
    """
    Recursive utility function to solve the N queens problem.

    Args:
        board (list): The current state of the board.
        row (int): The current row being considered.
        result (list): A list to store the solutions.

    Returns:
        None
    """
    if row == len(board):
        result.append(list(enumerate(board)))
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            nqueens_util(board, row + 1, result)
            board[row] = -1


def nqueens(n):
    """
    Solve the N queens problem and print all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    result = []
    nqueens_util(board, 0, result)

    for solution in result:
        print([list(pair) for pair in solution])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
