year = int(input())
print("Leap" if (not year % 4 and year % 100) or not year % 400 else "Ordinary")
