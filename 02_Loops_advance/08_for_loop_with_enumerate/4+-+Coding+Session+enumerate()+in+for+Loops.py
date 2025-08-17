# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

# Goal: multiply elements at odd indices by 2.
nums_list = [1, 5, 7, 9, 6, 12, 3]

for index, num in enumerate(nums_list):
    if index % 2 != 0:
        nums_list[index] = num * 2

print(nums_list)

# Previously, without enumerate...

for i in range(len(nums_list)):
   if nums_list[i] % 2 != 0:
       nums_list[i] = nums_list[i] * 2

print(nums_list)
