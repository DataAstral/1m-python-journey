# 4. Skip with continue — skip numbers divisible by 3
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)
