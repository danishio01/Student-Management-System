
students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")

        students.append({"name": name, "age": age})
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for i, student in enumerate(students, 1):
                print(f"{i}. {student['name']} - Age: {student['age']}")

    elif choice == "3":
        name = input("Enter name to search: ")
        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print(f"Found: {student['name']} - Age: {student['age']}")
                found = True

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
