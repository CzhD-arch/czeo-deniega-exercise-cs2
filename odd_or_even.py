import math

# Ask for number
number = int(input("Enter your number:"))
# Calculate the remainder
remainder = number % 2
# Select if the number is odd or even based on the remainder
if remainder == 1:
    print(f"{number} is odd.")
if remainder == 0:
    print(f"{number} is even.")
