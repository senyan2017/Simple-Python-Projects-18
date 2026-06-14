#!/usr/bin/env python
# coding: utf-8
"""Pure arithmetic helpers used by the Calculator script."""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    # Raises ZeroDivisionError on a zero divisor; the CLI turns that into a
    # friendly message so callers that reuse this stay free to handle it.
    return x / y


# Maps the menu choice to its (symbol, function) so the CLI stays data-driven
# instead of repeating an if/elif chain.
OPERATIONS = {
    "1": ("+", add),
    "2": ("-", subtract),
    "3": ("*", multiply),
    "4": ("/", divide),
}
