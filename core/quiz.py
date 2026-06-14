#!/usr/bin/env python
# coding: utf-8
"""Quiz data, scoring logic, and the interactive runner."""


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# Quiz content lives here so new questions can be added without touching logic.
QUESTIONS = [
    Question(
        "What is the level of Lake Urmia?\n(a) 120 meters\n(b) 100 meters\n(c) 135 meters\n\n",
        "c",
    ),
    Question(
        "Which category of languages does Python belong to?\n(a) programming languages\n(b) debugging languages\n(c) both\n\n",
        "a",
    ),
    Question(
        "Which city is the capital of Iran?\n(a) Tabriz\n(b) Mashhad\n(c) Tehran\n\n",
        "c",
    ),
]


def score_quiz(questions, answers):
    """Return how many answers match their question (pure, easy to test)."""
    return sum(
        1 for question, answer in zip(questions, answers) if answer == question.answer
    )


def run_quiz(questions=QUESTIONS):
    """Ask each question, then report the score. Wraps score_quiz for the I/O."""
    answers = []
    for question in questions:
        answers.append(input(question.prompt))
        print("--------------------------------------------------")
    score = score_quiz(questions, answers)
    print("You answered {} of {} questions correctly.".format(score, len(questions)))
    return score
