# Print only words longer than 3 characters
words = ["hi", "hello", "ok", "python", "go"]

for w in words:
    if len(w) <= 3:
        continue
    print(w)
