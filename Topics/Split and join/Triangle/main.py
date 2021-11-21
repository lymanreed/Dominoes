size = int(input())
hashes = 1
for line in range(1, size + 1):
    print(' ' * (size - line), end='')
    print('#' * hashes)
    hashes += 2
