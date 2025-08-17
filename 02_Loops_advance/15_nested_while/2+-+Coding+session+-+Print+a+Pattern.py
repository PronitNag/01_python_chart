# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

num_rows = 5
i = 1

while i <= num_rows:
    j = 1
    while j <= i:
        print(i * 2, end=" ")
        j += 1
    i += 1
    print()
