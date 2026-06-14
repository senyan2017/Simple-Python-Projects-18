"""
Pure quiz-scoring logic.

The Question class, the default question bank, and the scoring function
are all kept free of I/O so they can be imported and tested independently.
"""


class Question:
    """A single quiz question with its correct answer."""

    def __init__(self, prompt, answer):
        """
        Parameters
        ----------
        prompt : str
            The full question text shown to the player (including choices).
        answer : str
            The correct answer key (e.g. "a", "b", "c").
        """
        self.prompt = prompt
        self.answer = answer


# ---------------------------------------------------------------------------
# Default question bank
#
# Kept here (not inside the quiz runner) so that adding or editing questions
# only requires touching this file.
# ---------------------------------------------------------------------------

DEFAULT_QUESTION_DATA = [
    (
        "What is the level of Lake Urmia?\n"
        "(a) 120 meters\n"
        "(b) 100 meters\n"
        "(c) 135 meters\n\n",
        "c",
    ),
    (
        "Which category of languages does Python belong to?\n"
        "(a) programming languages\n"
        "(b) debugging languages\n"
        "(c) both\n\n",
        "a",
    ),
    (
        "Which city is the capital of Iran?\n"
        "(a) Tabriz\n"
        "(b) Mashhad\n"
        "(c) Tehran\n\n",
        "c",
    ),
]


def build_default_questions():
    """Return a list of Question objects built from DEFAULT_QUESTION_DATA."""
    return [Question(prompt, answer) for prompt, answer in DEFAULT_QUESTION_DATA]


def check_answer(question, user_answer):
    """Return True if user_answer matches the question's correct answer."""
    return user_answer.strip().lower() == question.answer.strip().lower()


def score_quiz(questions, user_answers):
    """
    Score a quiz and return (correct_count, total).

    Parameters
    ----------
    questions : list[Question]
    user_answers : list[str]
        Must be the same length as `questions`.
    """
    correct = sum(
        1 for q, a in zip(questions, user_answers) if check_answer(q, a)
    )
    return correct, len(questions)
