# task_15_shop_filter.py
# Given a list of tuples (product, price).
# Print items cheaper than 2.0.

pythonshop = [
    ("milk", 1.2),
    ("bread", 0.9),
    ("eggs", 2.5),
    ("butter", 3.1),
    ("juice", 1.8)
]

for item, price in pythonshop:
    if price < 2:
        print(item, price)
