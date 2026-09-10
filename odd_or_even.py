import math

number = int(input("Enter your number:"))

remainder = number % 2

if remainder == 1:
    print(f"{number} is odd.")
if remainder == 0:
    print(f"{number} is even.")
