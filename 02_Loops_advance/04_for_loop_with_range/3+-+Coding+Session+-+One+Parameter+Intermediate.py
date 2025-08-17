# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

# Example: print a sequence of numbers.

for i in range(5):
    print(i + 2)

# range(5) --> 0, 1, 2, 3, 4
# 1st: i = 0 -> print(0 + 2) -> print(2)
# 2nd: i = 1 -> print(1 + 2) -> print(3)
# 3rd: i = 2 -> print(2 + 2) -> print(4)
# 4th: i = 3 -> print(3 + 2) -> print(5)
# 5th: i = 4 -> print(4 + 2) -> print(6)


# Example: find the sum of the integers
# from 1 to 10.

total_sum = 0

for i in range(11):
    total_sum += i

# range(11) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 
print(total_sum)


# Example: Iterate over the elements of a list.

vowels = ["a", "e", "i", "o", "u"]

for i in range(len(vowels)):
    vowels[i] = vowels[i].upper()

# range(len(vowels)) --> 0, 1, 2, 3, 4 
print(vowels)
