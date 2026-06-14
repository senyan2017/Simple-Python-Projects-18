#!/usr/bin/env python
# coding: utf-8

"""
Password Generator — generate a random password of a given length.

Core generation logic lives in logic/password_logic.py.
This file only handles the command-line prompt and output.
"""

from logic.password_logic import generate_password, DEFAULT_LENGTH, MIN_LENGTH, MAX_LENGTH
from logic.input_utils import get_int


def main():
    print(f"Password Generator (length {MIN_LENGTH}–{MAX_LENGTH}, default {DEFAULT_LENGTH})")
    length = get_int(f"Enter password length [{DEFAULT_LENGTH}]: ")

    if length < MIN_LENGTH or length > MAX_LENGTH:
        print(f"Length must be between {MIN_LENGTH} and {MAX_LENGTH}. Using default {DEFAULT_LENGTH}.")
        length = DEFAULT_LENGTH

    password = generate_password(length)
    print(f"Generated password ({length} chars): {password}")


if __name__ == "__main__":
    main()
