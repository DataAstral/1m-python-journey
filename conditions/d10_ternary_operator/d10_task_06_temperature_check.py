temperature = input("What is the temperature? (hot, warm, cold): ").lower()

if temperature in ("hot", "warm", "cold"):
    result = "Hot" if temperature == "hot" else "Cold" if temperature == "cold" else "Warm"
    print(result)
else:
    print("Please enter only: hot, warm, or cold")
