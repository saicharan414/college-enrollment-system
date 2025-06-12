# College Enrollment System

students = {}

def enroll_student():
    roll = input("Enter roll number: ").strip()
    if roll in students:
        print("Student already enrolled.")
        return
    name = input("Enter student name: ").strip()
    students[roll] = {
        'name': name,
        'courses': []
    }
    print(f"Student {name} enrolled successfully.")

def assign_courses():
    roll = input("Enter roll number: ").strip()
    if roll not in students:
        print("Student not found.")
        return
    print("Enter course names separated by commas (e.g., Math,Science):")
    courses = input("Courses: ").strip().split(',')
    courses = [course.strip() for course in courses]
    students[roll]['courses'].extend(courses)
    print("Courses assigned successfully.")

def view_student_details():
    roll = input("Enter roll number: ").strip()
    if roll not in students:
        print("Student not found.")
        return
    student = students[roll]
    print(f"\n--- Student Details ---")
    print(f"Name: {student['name']}")
    print(f"Roll Number: {roll}")
    print("Courses:", ', '.join(student['courses']) if student['courses'] else "None")

def main():
    while True:
        print("\n=== College Enrollment System ===")
        print("1. Enroll Student")
        print("2. Assign Courses")
        print("3. View Student Details")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            enroll_student()
        elif choice == '2':
            assign_courses()
        elif choice == '3':
            view_student_details()
        elif choice == '4':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
