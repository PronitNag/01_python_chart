# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

grades = {}

print("==== Welcome to this Tool ===")

while True:
    
    print("Enter the name of the student:")
    while True:
        name = input()
        if name.isalpha():
            break
        else:
            print("Please enter a valid name.")
            
    print("Enter the grade:")
    while True:
        grade = input()
        if grade.isnumeric() and  (0 <= int(grade) <= 100):
            break
        else:
            print("Please enter a valid grade.")

    grades[name] = grade

    print("Grade recorded.\n")
    print("Would you like to enter the grade of another student?")
    print("Enter 1 for 'yes' and 0 for 'no'")

    stop = False
    
    while True:
        answer = int(input())        
        if answer == 0:
            stop = True
            break
        elif answer == 1:
            break
        elif (answer != 0) and (answer != 1):
            print("Please enter a valid option.")
    print()

    if stop:
        break

print("=== Final Grades ===")
for student, grade in grades.items():
    print(f"{student}: {grade}")
