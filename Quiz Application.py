#!/usr/bin/env python
# coding: utf-8
"""Runs the multiple-choice quiz. Questions and scoring live in core/quiz.py."""

from core.quiz import QUESTIONS, run_quiz


def main():
    run_quiz(QUESTIONS)


if __name__ == "__main__":
    main()
