# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

data = []

print("=== Enter Data ===")
print("To stop, please enter -1.")

while True:
    num = int(input("Value: "))
    if num == -1:
        break
    data.append(num)

print("== Final Dataset ==")
print(data)
