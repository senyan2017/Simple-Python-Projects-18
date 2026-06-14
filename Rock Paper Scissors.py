#!/usr/bin/env python
# coding: utf-8

"""
Rock Paper Scissors — play one round against the computer.

Winner determination and choice validation live in logic/rps_logic.py.
This file only handles the interactive prompt and output.
"""

from logic.rps_logic import get_computer_choice, determine_winner, is_valid_choice, CHOICES
from logic.input_utils import get_choice


def main():
    print("Let's play Rock, Paper, Scissors!")
    print("---------------------------------")

    user_choice = get_choice(
        f"Enter your choice ({'/'.join(CHOICES)}): ", CHOICES
    )
    computer_choice = get_computer_choice()

    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.\n")

    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    main()
