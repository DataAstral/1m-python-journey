# task_12_average_temp.py
# Given a tuple temps for 7 days.
# Calculate the average temperature.

temps = (22, 19, 25, 30, 17, 28, 21)
total = sum(temps)
result = total / len(temps)
print(result)
