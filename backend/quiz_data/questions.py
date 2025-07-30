import random

questions = [
    {
        "id": 1,
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "id": 2,
        "question": "Which language is used for web apps?",
        "options": ["Python", "JavaScript", "HTML", "All of the above"],
        "answer": "All of the above"
    },
    {
        "id": 3,
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "22"],
        "answer": "4"
    }
]

def get_random_questions(n=2):
    return random.sample(questions, min(n, len(questions)))
