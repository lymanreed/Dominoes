import math


angle = int(input())
angle = math.radians(angle)
cotangent = 1 / math.tan(angle)
print(round(cotangent, 10))
