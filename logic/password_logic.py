"""
Pure password-generation logic.

The default character set includes ASCII letters, digits and punctuation,
matching the original script.  Callers can override it if they need a
different alphabet.
"""

import random
import string

# The character set used by default — exposed so callers can inspect or extend it
DEFAULT_CHARACTERS = string.ascii_letters + string.digits + string.punctuation

# Sensible bounds exposed as named constants
MIN_LENGTH = 4
MAX_LENGTH = 128
DEFAULT_LENGTH = 10


def generate_password(length=DEFAULT_LENGTH, characters=DEFAULT_CHARACTERS):
    """
    Return a randomly generated password of the given length.

    Parameters
    ----------
    length : int
        Number of characters in the password (must be > 0).
    characters : str
        The pool of characters to sample from.

    Raises
    ------
    ValueError
        If length < 1 or characters is empty.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    if not characters:
        raise ValueError("Character pool must not be empty.")
    return "".join(random.choice(characters) for _ in range(length))
