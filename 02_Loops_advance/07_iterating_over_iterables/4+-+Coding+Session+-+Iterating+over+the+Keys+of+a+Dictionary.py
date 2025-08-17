# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

chemical_elements = {
    "Hydrogen": "H",
    "Helium": "He",
    "Beryllium": "Be",
    "Boron": "B",
    "Carbon": "C",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Fluorine": "F",
    "Neon": "Ne"
}

print(list(chemical_elements.keys()))

for elem in chemical_elements.keys():
    print(elem)

# Equivalent
for elem in chemical_elements:
    print(elem)
