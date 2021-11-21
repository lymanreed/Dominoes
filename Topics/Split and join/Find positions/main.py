numbers = input().split()
x = input()
x_positions = [str(i) for i in range(len(numbers)) if numbers[i] == x]
print(' '.join(x_positions) if len(x_positions) != 0 else "not found")
