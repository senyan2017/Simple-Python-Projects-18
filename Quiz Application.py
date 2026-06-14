#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What is the level of Lake Urmia?\n(a) 120 meters\n(b) 100 meters\n(c) 135 meters\n\n",
    "Which category of languages does Python belong to?\n(a) programming languages\n(b) debugging languages\n(c) both\n\n",
    "Which city is the capital of Iran?\n(a) Tabriz\n(b) Mashhad\n(c) Tehran\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

def run_quiz(questions):
    score = 0
    results = []
    for i, question in enumerate(questions, 1):
        raw_answer = input(question.prompt)
        answer = raw_answer.strip().lower()
        correct = answer == question.answer
        if correct:
            score += 1
        results.append((i, correct, question.answer, answer))
        print("--------------------------------------------------")

    print("You answered {} of {} questions correctly.".format(score, len(questions)))
    print("\n--- Results ---")
    for idx, correct, correct_answer, user_answer in results:
        status = "Correct" if correct else "Wrong"
        display_answer = user_answer if user_answer else "(empty)"
        print("Question {}: {} (your answer: {}, correct answer: {})".format(
            idx, status, display_answer, correct_answer))

run_quiz(questions)
