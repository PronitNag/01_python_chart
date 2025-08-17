# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

continue_loop = True

while continue_loop:
    print("Please enter two integers:")
    num1 = int(input())
    num2 = int(input())
    print(f"{num1} + {num2} is: {num1 + num2}")

    print("Would you like to enter two new integers?")
    ans = input("Please enter 'yes' or 'no': ")

    if ans == "no":
        continue_loop = False
