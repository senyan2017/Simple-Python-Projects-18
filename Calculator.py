#!/usr/bin/env python
# coding: utf-8
"""Command-line calculator. The arithmetic lives in core/calculator.py."""

from core.calculator import OPERATIONS
from core.cli_helpers import prompt_choice, prompt_float


def main():
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = prompt_choice("Enter choice (1-4):", OPERATIONS.keys())
    num1 = prompt_float("Enter first number:")
    num2 = prompt_float("Enter second number:")

    symbol, operation = OPERATIONS[choice]
    try:
        result = operation(num1, num2)
    except ZeroDivisionError:
        result = "Error: Cannot divide by zero"
    print(num1, symbol, num2, "=", result)


if __name__ == "__main__":
    main()
