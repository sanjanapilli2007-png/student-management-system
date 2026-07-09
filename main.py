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
    
