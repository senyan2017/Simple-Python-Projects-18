"""
Pure Tic-Tac-Toe game logic.

The board is a 3×3 list of single-character strings.
Empty cells are represented by a space (" ").
All functions here are side-effect free — no print / input calls.
"""

# Board dimensions — exposed so callers can build variant boards if desired
BOARD_SIZE = 3
EMPTY = " "
PLAYERS = ("X", "O")


def create_board():
    """Return a fresh, empty 3×3 board."""
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def check_win(board, player):
    """Return True if `player` has three in a row / column / diagonal."""
    n = len(board)
    # Rows and columns
    for i in range(n):
        if all(board[i][j] == player for j in range(n)):
            return True
        if all(board[j][i] == player for j in range(n)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(n)):
        return True
    if all(board[i][n - 1 - i] == player for i in range(n)):
        return True
    return False


def is_draw(board):
    """Return True when the board is full and nobody has won."""
    return all(cell != EMPTY for row in board for cell in row)


def is_valid_move(board, row, col):
    """Return True when (row, col) is inside the board and still empty."""
    n = len(board)
    if not (0 <= row < n and 0 <= col < n):
        return False
    return board[row][col] == EMPTY


def make_move(board, row, col, player):
    """
    Place `player`'s mark at (row, col) and return a new board.

    The original board is not mutated.
    Raises ValueError if the move is invalid.
    """
    if not is_valid_move(board, row, col):
        raise ValueError(f"Invalid move: ({row}, {col})")
    new_board = [row[:] for row in board]
    new_board[row][col] = player
    return new_board


def next_player(current_player):
    """Return the other player."""
    return "O" if current_player == "X" else "X"


def board_to_rows(board):
    """Flatten the board into a list of 9 cell values (top-left → bottom-right)."""
    return [cell for row in board for cell in row]
