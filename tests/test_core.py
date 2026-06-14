#!/usr/bin/env python
# coding: utf-8
"""Basic checks that the extracted core logic behaves as expected.

Run from the repository root with:  python -m unittest discover
"""

import unittest
from unittest import mock

from core import cli_helpers
from core.calculator import OPERATIONS, add, divide, multiply, subtract
from core.password import CHARACTER_SET, DEFAULT_LENGTH, generate_password
from core.quiz import QUESTIONS, Question, score_quiz
from core.tic_tac_toe import check_win, is_full, new_board, render_board


class CalculatorTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_operations_table(self):
        self.assertEqual(set(OPERATIONS), {"1", "2", "3", "4"})
        symbol, func = OPERATIONS["1"]
        self.assertEqual(symbol, "+")
        self.assertEqual(func(2, 2), 4)


class PasswordTests(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(generate_password(16)), 16)

    def test_default_length(self):
        self.assertEqual(len(generate_password()), DEFAULT_LENGTH)

    def test_uses_allowed_characters(self):
        password = generate_password(50)
        self.assertTrue(all(ch in CHARACTER_SET for ch in password))


class QuizTests(unittest.TestCase):
    def test_score_all_correct(self):
        answers = [question.answer for question in QUESTIONS]
        self.assertEqual(score_quiz(QUESTIONS, answers), len(QUESTIONS))

    def test_score_none_correct(self):
        answers = ["z" for _ in QUESTIONS]
        self.assertEqual(score_quiz(QUESTIONS, answers), 0)

    def test_score_partial(self):
        questions = [Question("p1", "a"), Question("p2", "b")]
        self.assertEqual(score_quiz(questions, ["a", "x"]), 1)


class TicTacToeTests(unittest.TestCase):
    def test_new_board_is_empty(self):
        board = new_board()
        self.assertEqual(len(board), 3)
        self.assertTrue(all(len(row) == 3 for row in board))
        self.assertTrue(all(cell == " " for row in board for cell in row))

    def test_check_win_row(self):
        board = new_board()
        board[0] = ["X", "X", "X"]
        self.assertTrue(check_win(board, "X"))
        self.assertFalse(check_win(board, "O"))

    def test_check_win_column(self):
        board = new_board()
        for i in range(3):
            board[i][1] = "O"
        self.assertTrue(check_win(board, "O"))

    def test_check_win_diagonal(self):
        board = new_board()
        board[0][0] = board[1][1] = board[2][2] = "X"
        self.assertTrue(check_win(board, "X"))

    def test_no_win_on_empty_board(self):
        self.assertFalse(check_win(new_board(), "X"))

    def test_is_full(self):
        self.assertFalse(is_full(new_board()))
        full = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
        self.assertTrue(is_full(full))

    def test_render_board_returns_string_with_marks(self):
        board = new_board()
        board[0][0] = "X"
        rendered = render_board(board)
        self.assertIsInstance(rendered, str)
        self.assertIn("X", rendered)


class CliHelperTests(unittest.TestCase):
    def test_prompt_int_retries_until_valid(self):
        with mock.patch("builtins.input", side_effect=["abc", "9", "1"]):
            with mock.patch("builtins.print"):
                self.assertEqual(cli_helpers.prompt_int("> ", 0, 2), 1)

    def test_prompt_choice_retries(self):
        with mock.patch("builtins.input", side_effect=["x", "2"]):
            with mock.patch("builtins.print"):
                self.assertEqual(cli_helpers.prompt_choice("> ", ["1", "2"]), "2")

    def test_prompt_float_retries(self):
        with mock.patch("builtins.input", side_effect=["nope", "3.5"]):
            with mock.patch("builtins.print"):
                self.assertEqual(cli_helpers.prompt_float("> "), 3.5)


if __name__ == "__main__":
    unittest.main()
