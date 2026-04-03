#Ternary operator in Python 6
temperature = input("What is the temperature? (hot, warm, cold): ").lower()
result = "Hot" if temperature == "hot" else "Cold" if temperature == "cold" else "Warm"
print(result)

# Ternary operator in Python 6.1
temperature = input("What is the temperature? (hot, warm, cold): ").lower()
if temperature in ("hot", "warm", "cold"):
    result = "Hot" if temperature == "hot" else "Cold" if temperature == "cold" else "Warm"
    print(result)
else:
    print("Please enter only: hot, warm, or cold")
