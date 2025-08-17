# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

for i in range(2, 4):
    for j in range(2):
        if (i + j) % 2 == 0:
            continue
        print(i, j)
