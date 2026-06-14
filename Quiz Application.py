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
    for index, question in enumerate(questions, start=1):
        user_answer = input(question.prompt)
        print("--------------------------------------------------")
        given = user_answer.strip()
        is_correct = given.lower() == question.answer.strip().lower()
        if is_correct:
            score += 1
        results.append((index, is_correct, given, question.answer.strip()))
    print("You answered {} of {} questions correctly.".format(score, len(questions)))
    print("==================================================")
    print("Review:")
    for index, is_correct, given, correct_answer in results:
        status = "Correct" if is_correct else "Wrong"
        shown = given if given else "(no answer)"
        print("Question {}: {} | your answer: '{}' | correct answer: '{}'".format(
            index, status, shown, correct_answer))

run_quiz(questions)

