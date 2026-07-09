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
    
