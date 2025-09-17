import random

QUESTIONS_FILE = "/home/user/Desktop/Python/file handling/Simple Quiz Game/questions.txt"

def load_questions():
    questions = []
    try:
        with open(QUESTIONS_FILE, "r") as f:
            for line in f:
                if "|" in line:
                    question, answer = line.strip().split("|")
                    questions.append({"question": question, "answer": answer})
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
    for i in questions:
        print(f"\nQ{question_number}. {i['question']}")
        answer = input("Your answer: ").strip()

        if answer.lower() == i["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f" Wrong! Correct Answer: {i['answer']}")

        question_number += 1  

    print(f"\n Final Score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
