#!/usr/bin/env python
# coding: utf-8

"""
Tic Tac Toe — two-player terminal game.

Board management, win/draw detection, and move validation live in
logic/tictactoe_logic.py.  This file only handles the display and
the interactive input loop.
"""

from logic.tictactoe_logic import (
    create_board, check_win, is_draw, is_valid_move,
    make_move, next_player, PLAYERS,
)
from logic.input_utils import get_int, print_separator


def draw_board(board):
    """Print the board in a human-readable format."""
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print("\n-------------")


def main():
    board = create_board()
    current_player = PLAYERS[0]

    while True:
        draw_board(board)

        row = get_int(f"Player {current_player} — row selection (0-2): ")
        col = get_int(f"Player {current_player} — column selection (0-2): ")

        if not is_valid_move(board, row, col):
            print("This cell is already taken or out of range. Please try again.")
            continue

        board = make_move(board, row, col, current_player)

        if check_win(board, current_player):
            draw_board(board)
            print(f"Player {current_player}, you won!")
            break

        if is_draw(board):
            draw_board(board)
            print("It's a draw!")
            break

        current_player = next_player(current_player)


if __name__ == "__main__":
    main()
