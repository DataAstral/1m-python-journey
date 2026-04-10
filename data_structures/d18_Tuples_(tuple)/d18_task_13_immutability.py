# task_13_immutability.py
# Create a tuple coords = (10, 20).
# Try to change the first element and catch the error.

coords = (10, 20)
try:
    coords[0] = 50
except TypeError:
    print("A tuple cannot be changed.")
