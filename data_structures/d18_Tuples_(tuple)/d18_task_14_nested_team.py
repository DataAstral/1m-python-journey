# task_14_nested_team.py
# Given a tuple of team members and their roles.
# Print: "Alice works as developer", etc.

pythonteam = (("Alice", "developer"), ("Bob", "designer"), ("Clara", "manager"))
for name, job in pythonteam:
    print(f"{name} works as {job}")
