# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

months = ["January", "February", "March"]

first_product = [530, 545, 670]
second_product = [250, 210, 295]
third_product = [715, 692, 850]

for month, prod1, prod2, prod3 in zip(months, first_product, second_product, third_product):
    total = prod1 + prod2 + prod3
    print(f"-> Total revenue in {month}")
    print(total)
