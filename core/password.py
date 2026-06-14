#!/usr/bin/env python
# coding: utf-8
"""Password generation logic and its default configuration."""

import random
import string

# Default configuration kept here so it is easy to tweak without touching logic.
CHARACTER_SET = string.ascii_letters + string.digits + string.punctuation
DEFAULT_LENGTH = 10


def generate_password(length=DEFAULT_LENGTH):
    """Return a random password of ``length`` characters from CHARACTER_SET."""
    return "".join(random.choice(CHARACTER_SET) for _ in range(length))
