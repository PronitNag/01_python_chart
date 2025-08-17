# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

words = ["Vehicle", "Noon", "Kayak", "Child", "Anna", "Mother", "May"]

palindromes = []

def is_palindrome(word):
    return word == word[::-1]

for word in words:
    if not is_palindrome(word.lower()):
        continue
    palindromes.append(word)

print(palindromes)
