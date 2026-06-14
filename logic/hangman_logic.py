"""
Pure Hangman game logic.

Word list, masked-word rendering, and guess validation are all kept
free of I/O so they can be imported and tested independently.
"""

import random

# Default word list — kept here so adding words only requires touching this file
DEFAULT_WORD_LIST = [
    "apple", "banana", "cherry", "date",
    "elderberry", "fig", "grape",
]

DEFAULT_MAX_TRIES = 6


def pick_random_word(word_list=DEFAULT_WORD_LIST):
    """Return a random word from the given list."""
    return random.choice(word_list)


def get_masked_word(secret, guessed_letters):
    """
    Return the display string for the current game state.

    Letters in `guessed_letters` are revealed; others appear as '_'.
    """
    return "".join(ch if ch in guessed_letters else "_" for ch in secret)


def is_valid_guess(letter):
    """Return True if `letter` is a single alphabetic character."""
    return len(letter) == 1 and letter.isalpha()


def is_word_guessed(secret, guessed_letters):
    """Return True when every letter in `secret` has been guessed."""
    return all(ch in guessed_letters for ch in secret)
