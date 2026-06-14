#!/usr/bin/env python
# coding: utf-8

"""
Dice Simulation — roll one or more dice and display the results.

Rolling logic lives in logic/dice_logic.py.
This file only handles the interactive prompt and output.
"""

from logic.dice_logic import simulate_dice, DEFAULT_SIDES
from logic.input_utils import get_int


def main():
    num_rolls = get_int("Enter the number of dice rolls: ")
    if num_rolls <= 0:
        print("Please enter a positive number.")
        return

    results = simulate_dice(num_rolls, DEFAULT_SIDES)

    print("The results of the dice roll:")
    for i, result in enumerate(results, start=1):
        print(f"  Roll {i}: {result}")


if __name__ == "__main__":
    main()
