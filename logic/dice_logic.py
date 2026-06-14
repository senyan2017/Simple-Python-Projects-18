"""
Pure dice-rolling logic.
"""

import random

DEFAULT_SIDES = 6


def roll_dice(sides=DEFAULT_SIDES):
    """Return a single random roll result (1 … sides)."""
    return random.randint(1, sides)


def simulate_dice(num_rolls, sides=DEFAULT_SIDES):
    """
    Roll `num_rolls` dice and return a list of results.

    Raises ValueError if num_rolls < 0.
    """
    if num_rolls < 0:
        raise ValueError("num_rolls must be non-negative.")
    return [roll_dice(sides) for _ in range(num_rolls)]
