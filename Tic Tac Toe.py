#!/usr/bin/env python
# coding: utf-8
"""Two-player Tic Tac Toe. The board logic lives in core/tic_tac_toe.py."""

from core.cli_helpers import prompt_int
from core.tic_tac_toe import check_win, is_full, new_board, render_board


def main():
    board = new_board()
    current_player = "X"

    while True:
        print(render_board(board))

        row = prompt_int("Row selection (0-2): ", 0, 2)
        col = prompt_int("Column selection (0-2): ", 0, 2)

        # Placing the player's token if the chosen cell is free.
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("This house has already been selected. Please try another position.")
            continue

        if check_win(board, current_player):
            print(render_board(board))
            print("player", current_player, "you won!")
            break

        if is_full(board):
            print(render_board(board))
            print("It's a draw!")
            break

        # Change the player's turn.
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
