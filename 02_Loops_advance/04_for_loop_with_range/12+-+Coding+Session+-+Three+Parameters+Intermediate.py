# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

# Example:

word = "Hello world"

for i in range(1, len(word), 2):
   print(word[i].capitalize())

# range(1, len(word), 2)
# 1, 2, 4, ..., 10

# Example:

n = 50
odd_numbers = []

for i in range(1, n, 2):
   odd_numbers.append(i)

print(odd_numbers)

# range(1, n, 2)
# 1, 3, 5, 7, ..., 49
