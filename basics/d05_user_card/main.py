# Store user information
first_name = "Anna"
last_name = "Smith"
age = 25
city = "London"

# Calculate birth year
current_year = 2025
born = current_year - age

# Print formatted user card
print("=== USER CARD ===")
print(f"Name: {first_name} {last_name[0]}.")   # First name + first letter of last name
print(f"Age: {age}")                          # User age
print(f"City: {city.upper()}")                # City in uppercase
print(f"Born: {born}")                        # Calculated birth year
print(f"Username: {first_name.lower()}_{last_name.lower()}")  # Username format
