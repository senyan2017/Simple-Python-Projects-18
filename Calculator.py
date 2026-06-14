#!/usr/bin/env python
# coding: utf-8

"""
Calculator — interactive command-line calculator.

Core arithmetic logic lives in logic/calculator_logic.py.
This file only handles the user-facing menu and input flow.
"""

from logic.calculator_logic import OPERATIONS
from logic.input_utils import get_float, get_choice


def main():
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = get_choice("Enter choice (1-4): ", list(OPERATIONS.keys()))

    num1 = get_float("Enter first number: ")
    num2 = get_float("Enter second number: ")

    symbol, operation = OPERATIONS[choice]
    result = operation(num1, num2)
    print(f"{num1} {symbol} {num2} = {result}")


if __name__ == "__main__":
    main()
