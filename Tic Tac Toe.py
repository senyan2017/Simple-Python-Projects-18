#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Function to draw the game screen
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

# Function to check game status
def check_win(board, player):

    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player or board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # Checking diameters
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check for a draw
def check_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

# Function to get a valid move from the player
def get_valid_move(board):
    while True:
        row_input = input("Row selection (0-2): ")
        col_input = input("Column selection (0-2): ")

        # Validate that inputs are digits within range
        try:
            row = int(row_input)
            col = int(col_input)
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Out of range. Please enter numbers between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("This house has already been selected. Please try another position.")
            continue

        return row, col

# The main function of the game
def play_game():

    # First, we clear the game screen
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Start the game with the turn of the first player (X)
    current_player = "X"

    while True:
        draw_board(board)

        # Check for draw before getting input
        if check_draw(board):
            print("The board is full. It's a draw!")
            break

        # Get a valid position from the current player
        row, col = get_valid_move(board)

        # Place the player's token on the game board
        board[row][col] = current_player

        # Check the current player's win
        if check_win(board, current_player):
            draw_board(board)
            print("player", current_player, "you won!")
            break

        # Change the player's turn
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
