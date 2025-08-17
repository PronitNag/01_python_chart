# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

print("Let's find a letter in a string:")
text = input("Enter the string: ")
target = input("Enter the letter: ")

for char in text:
    print("--> New Iteration")
    if char == target:
        print("Found it!")
        print("break")
        break
