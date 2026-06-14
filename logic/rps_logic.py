"""
Pure Rock-Paper-Scissors logic.

No I/O — suitable for import, reuse and testing.
"""

import random

CHOICES = ["rock", "paper", "scissors"]

# (user_choice, computer_choice) → result message
WIN_MAP = {
    ("rock", "scissors"): "You win!",
    ("paper", "rock"): "You win!",
    ("scissors", "paper"): "You win!",
}


def get_computer_choice():
    """Return a random choice from CHOICES."""
    return random.choice(CHOICES)


def determine_winner(user_choice, computer_choice):
    """
    Return a result string describing the outcome.

    Possible returns: "It's a tie!", "You win!", or "Computer wins!"
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    if WIN_MAP.get((user_choice, computer_choice)):
        return "You win!"
    return "Computer wins!"


def is_valid_choice(choice):
    """Return True if choice is one of CHOICES (case-insensitive)."""
    return choice.lower() in CHOICES
