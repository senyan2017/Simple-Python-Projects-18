#!/usr/bin/env python
# coding: utf-8

"""
Binary Search Algorithm — interactive demo of binary search.

The search algorithm itself lives in logic/binary_search_logic.py.
This file only handles the demo data and output.
"""

from logic.binary_search_logic import binary_search


def main():
    # Demo data — same example as the original script
    arr = [2, 4, 6, 8, 10]
    target = 8

    print(f"Sorted list: {arr}")
    print(f"Searching for: {target}")

    result = binary_search(arr, target)

    if result != -1:
        print(f"The desired number is at index {result}.")
    else:
        print("The desired number does not exist in the list.")


if __name__ == "__main__":
    main()
