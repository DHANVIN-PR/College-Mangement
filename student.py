students = []


def add_student():
    student_id = input("Student ID: ")
    name = input("Name: ")
    course = input("Course: ")
    students.append({"id": student_id, "name": name, "course": course})
    print("Student added.")


def search_student():
    student_id = input("Enter student ID: ")
    for student in students:
        if student["id"] == student_id:
            print(student)
            return
    print("Student not found.")


def display_students():
    for student in students:
        print(student)

