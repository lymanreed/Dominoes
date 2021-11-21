digits = int(input())
x = digits // 100
y = (digits % 100) // 10
z = (digits % 100) % 10
print(x + y + z)
