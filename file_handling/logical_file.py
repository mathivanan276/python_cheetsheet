# Write a function that reads a number from a file and returns its square.

# Curveballs:

# Handle cases where the file does not exist.

# Handle cases where the content is not a number.

# Handle very large numbers (potential overflow).

import os

path = os.path.dirname(os.path.abspath(__file__)) + "/number.txt"

try:
    with open(path, 'r') as f:
        number = f.readline().strip()
    
    if int(number):
        print(int(number) ** 2)
    else:
        raise ValueError("Invalid number")

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid number")
