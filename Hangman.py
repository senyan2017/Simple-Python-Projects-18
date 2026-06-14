#!/usr/bin/env python
# coding: utf-8

"""
Hangman — classic word-guessing game in the terminal.

Word list, masked-word rendering and guess validation live in
logic/hangman_logic.py.  This file only handles the game loop and display.
"""

from logic.hangman_logic import (
    pick_random_word, get_masked_word, is_valid_guess,
    is_word_guessed, DEFAULT_MAX_TRIES,
)
from logic.input_utils import print_separator


def main():
    secret = pick_random_word()
    guessed_letters = []
    tries = DEFAULT_MAX_TRIES

    print("Welcome to Hangman!")

    while tries > 0:
        masked = get_masked_word(secret, guessed_letters)

        if is_word_guessed(secret, guessed_letters):
            print(f"Word: {masked}")
            print("Congratulations! You won!")
            break

        print(f"Word: {' '.join(masked)}")
        print(f"Tries remaining: {tries}")

        guess = input("Guess a letter: ").lower()

        if not is_valid_guess(guess):
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret:
            print("Correct guess!")
        else:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")

        print_separator()

    if tries == 0:
        print(f"Game over! The word was: {secret}")


if __name__ == "__main__":
    main()
