import random

def run_quiz(questions):
    score = 0
    random.shuffle(questions)
    for idx, q in enumerate(questions, start=1):
        print(f"Question {idx}: {q['question']}")
        for i, opt in enumerate(q['options'], start=1):
            print(f"  {i}. {opt}")
        while True:
            try:
                choice = int(input("Your answer (1-{}): ".format(len(q['options']))))
                if 1 <= choice <= len(q['options']):
                    break
                else:
                    print("Please enter a valid option number.")
            except ValueError:
                print("Please enter a number.")
        if q['options'][choice-1].lower() == q['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}\n")
    print(f"You got {score} out of {len(questions)} correct.")

if __name__ == "__main__":
    question_bank = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "Which language is this quiz written in?",
            "options": ["Java", "C#", "Python", "JavaScript"],
            "answer": "Python"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Mark Twain", "William Shakespeare", "Charles Dickens", "Leo Tolstoy"],
            "answer": "William Shakespeare"
        },
    ]
    run_quiz(question_bank)
