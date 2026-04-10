# task_09_enumerate_cities.py
# Given a tuple cities.
# Print each city with its number starting from 1.

cities = ("Paris", "Berlin", "Rome", "Madrid", "Oslo")
for i, city in enumerate(cities, start=1):
    print(i, city)
