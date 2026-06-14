#!/usr/bin/env python
# coding: utf-8

"""
Typing Speed Test — measure how fast you can type a given sentence.

Speed and accuracy calculations live in logic/typing_speed_logic.py.
This file only handles the timing, input collection and result display.
"""

import time

from logic.typing_speed_logic import (
    calculate_wpm, calculate_accuracy, DEFAULT_SENTENCE,
)
from logic.input_utils import print_separator


def main():
    sentence = DEFAULT_SENTENCE

    print("Type this sentence as fast as you can:")
    print(sentence)
    print_separator()
    input("Press Enter when you are ready to start.\n")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    elapsed = end_time - start_time
    wpm = calculate_wpm(user_input, elapsed)
    accuracy = calculate_accuracy(user_input, sentence) * 100

    print_separator()
    print(f"Total time: {round(elapsed, 2)} seconds")
    print(f"Typing speed: {round(wpm, 2)} words per minute")
    print(f"Accuracy: {round(accuracy, 1)}%")


if __name__ == "__main__":
    main()
