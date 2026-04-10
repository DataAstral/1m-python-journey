# task_16_min_max_manual.py
# Given a tuple prices.
# Find the most expensive and cheapest values without min() and max().

prices = (120, 450, 89, 300, 55, 210)

max_price = prices[0]
min_price = prices[0]

for price in prices:
    if price > max_price:
        max_price = price
    if price < min_price:
        min_price = price

print("Most expensive:", max_price)
print("Cheapest:", min_price)
