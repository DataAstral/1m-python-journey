# Keep asking for text until the user types "stop"
while True:
    text = input("Enter text (or 'stop'): ")
    if text == "stop":
        break
    print("Here is your text:", text)
