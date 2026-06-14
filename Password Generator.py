#!/usr/bin/env python
# coding: utf-8
"""Prints a random password. The generation logic lives in core/password.py."""

from core.password import generate_password


def main():
    print(generate_password())


if __name__ == "__main__":
    main()
