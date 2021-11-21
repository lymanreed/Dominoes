offset = int(input())
zone = 10.5 + offset
print("Monday" if zone < 0 else "Wednesday" if zone >= 24 else "Tuesday")
