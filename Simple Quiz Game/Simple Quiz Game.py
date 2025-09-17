import random

QUESTIONS_FILE = "/home/user/Desktop/Python/file handling/Simple Quiz Game/questions.txt"

def load_questions():
    questions = []
    try:
        with open(QUESTIONS_FILE, "r") as f:
            for line in f:
                if "|" in line:
                    q, a = line.strip().split("|")
                    questions.append({"q": q, "a": a})
    except FileNotFoundError:
        print(" questions.txt file not found!")
    return questions

def quiz_game():
    questions = load_questions()
    if not questions:
        print("No questions available!")
        return

    random.shuffle(questions)  
    score = 0
    question_number = 1  

    print("\n--- Quiz Game ---")
    for qa in questions:
        print(f"\nQ{question_number}. {qa['q']}")
        answer = input("Your answer: ").strip()

        if answer.lower() == qa["a"].lower():
            print("Correct!")
            score += 1
        else:
            print(f" Wrong! Correct Answer: {qa['a']}")

        question_number += 1  

    print(f"\n Final Score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
