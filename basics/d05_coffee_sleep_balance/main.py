# 🧠 Program "Mood Calculator"

# Ask for the user's name
name = input("Enter your name: ")

# Greet the user
print("Hello " + name)

# Ask for the user's age
age = int(input("Enter your age: "))

# Ask for the user's mood
mood = input("Enter your mood: ")

# Ask for the number of coffee cups
coffee = int(input("Enter how many cups of coffee you had today: "))

# Ask how many hours the user slept
sleep_time = int(input("Enter how many hours you slept: "))

# Calculate balance between coffee and sleep
balance = coffee - sleep_time

# Show results
print("Today you feel", mood)
print("Your age is", age)
print("You drank", coffee, "cups of coffee today")
print("You slept for", sleep_time, "hours")

# Give simple advice
print("Advice: you should get more sleep")
