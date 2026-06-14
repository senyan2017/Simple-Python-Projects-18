#!/usr/bin/env python
# coding: utf-8

"""
Quiz Application — run a multiple-choice quiz in the terminal.

Question data and scoring logic live in logic/quiz_logic.py.
This file only handles the interactive question/answer loop and result output.
"""

from logic.quiz_logic import build_default_questions, check_answer, score_quiz
from logic.input_utils import print_separator


def main():
    questions = build_default_questions()
    user_answers = []

    print(f"Welcome to the Quiz! ({len(questions)} questions)")
    print_separator()

    for question in questions:
        answer = input(question.prompt).strip()
        user_answers.append(answer)
        if check_answer(question, answer):
            print("Correct!")
        else:
            print(f"Wrong — the correct answer was '{question.answer}'.")
        print_separator()

    correct, total = score_quiz(questions, user_answers)
    print(f"You answered {correct} of {total} questions correctly.")


if __name__ == "__main__":
    main()
