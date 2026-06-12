students = {}

while True:
    print("\n===== Student Result System =====")
    print("1. Add Student")
    print("2. View Results")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Student Name: ")
        marks = input("Marks: ")
        students[name] = marks
        print("Student Added")

    elif choice == "2":
        for name, marks in students.items():
            print(name, "-", marks)

    elif choice == "3":
        break

    else:
        print("Invalid Option")