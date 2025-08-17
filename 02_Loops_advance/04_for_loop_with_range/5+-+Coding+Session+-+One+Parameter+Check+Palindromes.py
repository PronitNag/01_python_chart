# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

word = "hannah"

is_palindrome = True

for i in range(len(word) // 2):
    left_char = word[i]
    right_char = word[len(word)-i-1]

    if left_char.lower() != right_char.lower():
        is_palindrome = False

print(is_palindrome)

# len(word) = 6
#       -----------------------
#         i   |  len(word)-i-1
#       -----------------------
# 1st:    0   |  6 - 0 - 1 = 5
# 2nd:    1   |  6 - 1 - 1 = 4
# 3rd:    2   |  6 - 2 - 1 = 3

#  h a n n a h
#  0 1 2 3 4 5

# Tests:
# Other palindromes: noon, level.
# Not palindromes: python, javascript.