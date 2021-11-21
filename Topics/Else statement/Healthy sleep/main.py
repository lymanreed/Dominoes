minimum = int(input())
maximum = int(input())
actual = int(input())

if actual < minimum:
    print("Deficiency")
else:
    if actual > maximum:
        print("Excess")
    else:
        print("Normal")
