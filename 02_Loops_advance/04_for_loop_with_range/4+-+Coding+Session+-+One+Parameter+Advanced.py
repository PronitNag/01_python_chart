# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

# Example

numbers = [2, 3, 4, 5, 6]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

# Example

numbers = [2, 3, 4, 5, 6]

for i in range(len(numbers)):
    elem = numbers[i]
    if elem % 2 == 0:
        print(f'{elem} is even.')
    else:
        print(f'{elem} is odd.')
