STUDENT_FILE = "/home/user/Desktop/Python/file handling/Student Marks Record/student.txt"


def student_tracker():
    """Load students from file"""
    student_details = []
    try:
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                student_name, mark = line.strip().split("|")
                student_details.append({
                    "student_name": student_name,
                    "mark": int(mark),
                })
    except FileNotFoundError:
        pass
    return student_details


def save_item(student_details):
    with open(STUDENT_FILE, "w") as f:
        for i in student_details:
            f.write(f"{i['student_name']}|{i['mark']}\n")


def add_student(student_details):
    student_name = input("Enter student name: ")
    while True:
        try:
            mark = int(input("Enter mark: "))
            break
        except ValueError:
            print(" Please enter a valid number for marks.")
    
    student_details.append({
        "student_name": student_name,
        "mark": mark,
    })
    save_item(student_details)
    print(" Student saved successfully!")
    
    view_all(student_details)


def view_all(student_details):
    if not student_details:
        print(" No students stored yet.")
        return
    print("\n--- Student Records ---")
    for c in student_details:
        print(f"Student: {c['student_name']}, Mark: {c['mark']}")


def calculate_average(student_details):
    if not student_details:
        print(" No students stored yet.")
        return
    total = sum(c['mark'] for c in student_details)
    avg = total / len(student_details)
    print(f" Average Marks: {avg:.2f}")


def top_scorer(student_details):
    if not student_details:
        print(" No students stored yet.")
        return


def main():
    students = student_tracker()
    while True:
        print("\n=== Student Marks Tracker ===")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Calculate Average Marks")
        print("4. Display Top Scorer")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            top_scorer(students)
        elif choice == "5":
            print(" Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
