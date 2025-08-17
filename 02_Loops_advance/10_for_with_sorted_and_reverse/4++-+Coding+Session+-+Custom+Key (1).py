# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

tuples = [("A", 5), ("B", 8), ("C", 0), ("D", 9)]

# Example 1

def get_last_elem(tuple):
    return tuple[-1]

for char, num in sorted(tuples, key=get_last_elem):
    print(char, num)

# Example 2

def get_first_elem(tuple):
    return tuple[0]

for char, num in sorted(tuples, key=get_first_elem):
    print(char, num)
