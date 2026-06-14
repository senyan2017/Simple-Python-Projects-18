#!/usr/bin/env python
# coding: utf-8
"""Pure board helpers for Tic Tac Toe (no game-flow input/print)."""

EMPTY = " "
SEPARATOR = "-------------"


def new_board():
    """Return a fresh empty 3x3 board."""
    return [[EMPTY for _ in range(3)] for _ in range(3)]


def render_board(board):
    """Return the board as a printable string."""
    lines = [SEPARATOR]
    for row in board:
        lines.append("|" + "".join(" {} |".format(cell) for cell in row))
        lines.append(SEPARATOR)
    return "\n".join(lines)


def check_win(board, player):
    """Return True if ``player`` has three in a row, column, or diagonal."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def is_full(board):
    """Return True if no empty cells remain (used to detect a draw)."""
    return all(cell != EMPTY for row in board for cell in row)
