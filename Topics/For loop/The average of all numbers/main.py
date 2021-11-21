a, b = int(input()), int(input())
sum_ = 0
count = 0
for i in range(a, b + 1):
    if not i % 3:
        sum_ += i
        count += 1
print(sum_ / count)
