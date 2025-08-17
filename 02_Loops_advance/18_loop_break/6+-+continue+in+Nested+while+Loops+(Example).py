# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

i = 0

while i < 2:
    j = 0
    while j < 3:
        j += 1
        if j % 2 == 0:
            continue
        print(i, j)
    i += 1
