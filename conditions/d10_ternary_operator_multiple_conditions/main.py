#Ternary operator in Python 5
mood = input("What is your mood?: (happy, sad, ok): ")
result = "happy" if mood == "happy" else "sad" if mood == "sad" else "ok"
print(f"Your mood is {result}")
