# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

# Print all the substrings of length 2
# excluding the first and last
# characters.

word = "programming"

for i in range(1, len(word)-2):
    print(word[i:i+2])

# p r o g r a m m i n g
# 0 1 2 3 4 5 6 7 8 9 10

