n = input()
print([(int(n[i]) + int(n[i + 1])) / 2 for i in range(len(n) - 1)])
