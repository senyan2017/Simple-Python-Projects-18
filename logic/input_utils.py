"""
Shared input utilities for interactive scripts.

Provides common helper functions for reading and validating user input,
so each script doesn't need to reimplement its own retry/validation loop.
"""


def get_float(prompt):
    """Prompt the user until a valid float is entered, then return it."""
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def get_int(prompt):
    """Prompt the user until a valid integer is entered, then return it."""
    while True:
        raw = input(prompt)
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")


def get_choice(prompt, valid_choices):
    """
    Prompt the user until one of `valid_choices` is entered.

    Comparison is case-insensitive; the returned value is always lowercase.
    """
    lower_choices = [c.lower() for c in valid_choices]
    while True:
        raw = input(prompt).strip().lower()
        if raw in lower_choices:
            return raw
        print(f"Invalid choice. Please enter one of: {', '.join(valid_choices)}")


def get_yes_no(prompt):
    """Prompt the user until 'y' or 'n' is entered. Returns True for 'y'."""
    while True:
        raw = input(prompt).strip().lower()
        if raw in ('y', 'yes'):
            return True
        if raw in ('n', 'no'):
            return False
        print("Please enter 'y' or 'n'.")


def print_separator(char="-", width=50):
    """Print a visual separator line."""
    print(char * width)
