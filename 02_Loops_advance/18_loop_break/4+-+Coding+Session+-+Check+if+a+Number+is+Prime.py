# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

import math

def find_divisors(num):
    divisors_list = [1, num]
    
    divisor = 2
    while divisor <= math.sqrt(num):
        if num % divisor == 0:
            divisors_list.append(divisor)
            divisors_list.append(num // divisor)
        divisor += 1
    
    return sorted(list(set(divisors_list)))

while True:
    print("Enter a positive integer to check if it is prime. Enter 's' to stop.")
    value = input()

    if value == 's':
        break
    
    if (not value.isnumeric()) or (int(value) <= 0):
        continue

    divisors = find_divisors(int(value))

    if len(divisors) == 2:
        print("This number is prime")
    else:
        print(f"The number {value} is not prime")
        print(f"Divisors: {divisors}")
