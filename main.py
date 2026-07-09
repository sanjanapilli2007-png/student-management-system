print("Welcome to Student Management System")

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "6":
        print("Thank you!")
        break
    else:
        print("Feature will be added soon.")
DESIGN PROGRAM FLOW:     
Project Planning → Done
↓
Create GitHub Repository → Done
↓
Design Program Flow → In Progress
↓
Edit main.py and commit the menu code
↓
Design Program Flow → Done
↓
Write Add Student Function → In Progress   
ADD STUDENT FUNCTION:
students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        department = input("Enter Department: ")

        student = {
            "Name": name,
            "Roll": roll,
            "Department": department
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(student)

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("This feature will be added later.")
VIEW STUDENT FUNCTION:
elif choice == "2":
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        for student in students:
            print(student)
WRITE SEARCH STUDENT FUNCTION:
elif choice == "3":
    roll = input("Enter Roll Number to search: ")

    found = False
    for student in students:
        if student["Roll"] == roll:
            print("\nStudent Found")
            print("Name:", student["Name"])
            print("Roll:", student["Roll"])
            print("Department:", student["Department"])
            found = True
            break

    if not found:
        print("Student not found.")
WRITE UPDATE STUDENT FUNCTION:
elif choice == "4":
    roll = input("Enter Roll Number to update: ")

    found = False
    for student in students:
        if student["Roll"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Department"] = input("Enter New Department: ")
            print("Student record updated successfully!")
            found = True
            break

    if not found:
        print("Student not found.")
WRITE DELETE STUDENT FUNCTION:
elif choice == "5":
    roll = input("Enter Roll Number to delete: ")

    found = False
    for student in students:
        if student["Roll"] == roll:
            students.remove(student)
            print("Student record deleted successfully!")
            found = True
            break

    if not found:
        print("Student not found.")
IMPLEMENT FILE HANDLING:
elif choice == "1":
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    department = input("Enter Department: ")

    student = {
        "Name": name,
        "Roll": roll,
        "Department": department
    }

    students.append(student)

    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{department}\n")

    print("Student added successfully!")
TEST THE PROGRAM:
ADD TWO STUDENTS.
VIEW THE STUDENTS
SEARCH FOR ONE BY ROLL NUMBER.
UPDATE STUDENTS DETAILS.
DELETE A STUDENT.
EXIT THE PROGRAM.


      
      
