#!/usr/bin/env python
# coding: utf-8

"""
Email Slicer — split an email address into username and domain.

Slicing logic lives in logic/email_slicer_logic.py.
This file only handles the user prompt and output.
"""

from logic.email_slicer_logic import slice_email


def main():
    email = input("Enter your email address: ")

    try:
        username, domain = slice_email(email)
        print("Username:", username)
        print("Domain:", domain)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
