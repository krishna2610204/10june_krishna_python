"""Create a mini-project where students combine conditional statements, loops, and functions
to create a basic Python application, such as a simple calculator or a grade management
system."""

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

# Function to display all student records
def display_students(records):
    if not records:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for name, marks in records.items():
        grade = calculate_grade(marks)
        print(f"Name: {name}, Marks: {marks}, Grade: {grade}")
    print("------------------------\n")

# Main program
students = {}

while True:
    print("\nGrade Management System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        name = input("Enter student name: ")
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                students[name] = marks
                print(f"{name}'s data added successfully!")
            else:
                print("Marks should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter numeric marks.")
    
    elif choice == '2':
        display_students(students)
    
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
