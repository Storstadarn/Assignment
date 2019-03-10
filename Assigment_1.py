students = ["Lucas", "Benjamin", "Tom", "Ian"]
student_name = input("What is your name? ")
if student_name in students:
    print("Welcome to the course!")
else:
    print("Access denied! Please enter your name to be added to the course!")
    while True:
        new_student = input("Enter your name: ")
        students.append(new_student)
        confirm_name = input("Welcome to the course! Confirm name. Is " + students[-1] + " your name? y/n: ")
        if confirm_name == "y":
            print("Access granted! Welcome " + students[-1] + "!")
            break
        else:
            del students[-1]
            print("Please enter your name again!")

