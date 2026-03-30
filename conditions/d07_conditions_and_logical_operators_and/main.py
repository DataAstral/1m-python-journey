#  Travel eligibility check

# Ask if the user has a passport
passport = input("Do you have a passport? (yes/no): ")

# Ask if the user has a visa
visa = input("Do you have a visa? (yes/no): ")

# Check both conditions
# If the user has both a passport and a visa → allow travel
if passport == "yes" and visa == "yes":
    print("You can travel abroad!")
# Otherwise → deny travel
else:
    print("You cannot travel.")
