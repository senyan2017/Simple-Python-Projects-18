#!/usr/bin/env python
# coding: utf-8

"""
Countdown Timer — count down from a given number of seconds.

Core countdown logic lives in logic/countdown_logic.py.
This file only handles the user prompt.
"""

from logic.countdown_logic import countdown
from logic.input_utils import get_int


def main():
    t = get_int("Enter the time in seconds: ")
    if t <= 0:
        print("Please enter a positive number.")
        return
    countdown(t)


if __name__ == "__main__":
    main()
