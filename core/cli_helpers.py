#!/usr/bin/env python
# coding: utf-8
"""Small shared helpers for command-line interaction.

These keep input validation, retry-on-error, and prompting consistent across
the interactive scripts, so each one does not reinvent the same input loop.
"""


def prompt_int(message, min_value=None, max_value=None):
    """Ask for an integer, repeating until a valid in-range value is given."""
    while True:
        raw = input(message)
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print("Please enter a number >= {}.".format(min_value))
            continue
        if max_value is not None and value > max_value:
            print("Please enter a number <= {}.".format(max_value))
            continue
        return value


def prompt_float(message):
    """Ask for a number, repeating until a valid value is given."""
    while True:
        raw = input(message)
        try:
            return float(raw)
        except ValueError:
            print("Please enter a number.")


def prompt_choice(message, valid_choices):
    """Ask for one of ``valid_choices``, repeating until the input matches."""
    choices = list(valid_choices)
    while True:
        answer = input(message).strip()
        if answer in choices:
            return answer
        print("Please choose one of: {}".format(", ".join(choices)))
