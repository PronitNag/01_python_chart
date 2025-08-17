# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

# Example 1: Reverse Casing

my_string = "Learning Loops"
new_string = ""

for char in my_string:
    if char.isupper():
        new_string += char.lower()
    else:
        new_string += char.upper()

print(new_string)

# Example 2: Remove duplicates

my_string = "aaabbcccddeffghhii"
new_string = ""

for char in my_string:
    if not char in new_string:
        new_string += char
    
print(new_string)
