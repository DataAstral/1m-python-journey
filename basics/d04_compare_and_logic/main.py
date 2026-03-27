# Ask the user for two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Comparison operators
print("a == b:", a == b)   # Equal
print("a != b:", a != b)   # Not equal
print("a > b:", a > b)     # Greater than
print("a < b:", a < b)     # Less than
print("a >= b:", a >= b)   # Greater than or equal to
print("a <= b:", a <= b)   # Less than or equal to

# Logical expressions
print("Both are positive:", a > 0 and b > 0)
print("At least one is positive:", a > 0 or b > 0)
print("a is not positive:", not (a > 0))
