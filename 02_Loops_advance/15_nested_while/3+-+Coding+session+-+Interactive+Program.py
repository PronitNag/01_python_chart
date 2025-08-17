# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

grades = {}
continue_loop = True

print("===== Welcome to this Interactive Tool =====")

while continue_loop:
    
    print("Enter the name of the student:")
    is_valid = False
    while not is_valid:
        name = input()
        if name.isalpha():
            is_valid = True
        else:
            print("Please enter a valid name.")
            
    print("Enter the final grade:")
    is_valid = False
    while not is_valid:
        grade = input()
        if grade.isnumeric() and  (0 <= int(grade) <= 100):
            is_valid = True
        else:
            print("Please enter a valid grade.")

    grades[name] = grade

    print("Grade recorded.\n")
    print("Would you like to enter the grade of another student?")
    print("Enter 1 for 'yes' and 0 for 'no'.")

    is_valid = False
    while not is_valid:
        answer = int(input())        
        if answer == 0:
            is_valid = True
            continue_loop = False
        elif answer == 1:
            is_valid = True
        else:
            print("Please enter a valid option.")
    print()

print("=== Final Grades ===")
for student, grade in grades.items():
    print(f"{student}: {grade}")
