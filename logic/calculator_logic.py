"""
Pure arithmetic operations for the Calculator script.

All functions are side-effect free (no print / input) so they can be
imported and reused anywhere without triggering I/O.
"""


def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return the difference of x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """
    Return the quotient of x and y.

    Returns the string "Error: Cannot divide by zero" when y is zero,
    matching the original script's behaviour.
    """
    if y != 0:
        return x / y
    return "Error: Cannot divide by zero"


# Maps menu choice strings → (display symbol, operation function)
OPERATIONS = {
    "1": ("+", add),
    "2": ("-", subtract),
    "3": ("*", multiply),
    "4": ("/", divide),
}
