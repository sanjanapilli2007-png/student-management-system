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
