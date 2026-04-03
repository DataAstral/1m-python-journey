# Try to convert a string into an integer
try:
    x = int("abc")

# Catch the error and save it into variable 'e'
except ValueError as e:
    # Print the error message
    print(f"Error: {e}")

# → Error: invalid literal for int() with base 10: 'abc'