# TASK 10 — SECOND MAX

nums = [3, 7, 1, 9, 4, 6, 9, 2]

first_max = max(nums)
second_max = None

for n in nums:
    if n == first_max:
        continue
    if second_max is None or n > second_max:
        second_max = n

print(second_max)
