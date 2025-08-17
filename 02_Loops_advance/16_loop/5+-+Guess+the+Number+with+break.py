# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

low = 0
high = 1000
answer = (low + high) // 2

print("======================================")
print("Welcome to the 'Guess the Number' game")
print("======================================")

print(f"Think of an integer between {low} and {high}...")

num_iterations = 0

while True:
    num_iterations += 1

    print(f"\nIs {answer} the number?")
    print("Enter 1 if the guess is too low")
    print("Enter 2 if the guess is too high")
    print("Enter 3 if the guess is correct")

    user_input = int(input("Answer: "))

    if user_input == 1:
        low = answer
    elif user_input == 2:
        high = answer
    elif user_input == 3:
        print(f"\nFound it! The number is: {answer}")
        if num_iterations == 1:
            print("It only took one iteration.")
        else:
            print(f"It only took {num_iterations} iterations.")
        break
    else:
        print("Enter a valid option.")

    answer = (low + high) // 2
