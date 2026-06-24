import json

FILE_NAME = "students.json"

# Load data from file
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add student
def add_student(data):
    try:
        student_id = input("Enter ID: ")
        if student_id in data:
            print("Student already exists!")
            return

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        data[student_id] = {
            "name": name,
            "age": age,
            "course": course
        }

        save_data(data)
        print("Student added successfully!")

    except ValueError:
        print("Invalid input!")

# View all students
def view_students(data):
    if not data:
        print("No records found.")
        return

    for sid, info in data.items():
        print(f"\nID: {sid}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Course: {info['course']}")

# Search student
def search_student(data):
    student_id = input("Enter ID to search: ")

    if student_id in data:
        info = data[student_id]
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print(f"Course: {info['course']}")
    else:
        print("Student not found.")

# Update student
def update_student(data):
    student_id = input("Enter ID to update: ")

    if student_id in data:
        try:
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            course = input("Enter new course: ")

            data[student_id] = {
                "name": name,
                "age": age,
                "course": course
            }

            save_data(data)
            print("Student updated successfully!")

        except ValueError:
            print("Invalid input!")
    else:
        print("Student not found.")

# Delete student
def delete_student(data):
    student_id = input("Enter ID to delete: ")

    if student_id in data:
        del data[student_id]
        save_data(data)
        print("Student deleted successfully!")
    else:
        print("Student not found.")

# Main menu
def main():
    data = load_data()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            update_student(data)
        elif choice == "5":
            delete_student(data)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()