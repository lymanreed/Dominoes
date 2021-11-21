string = input()
new = [c for c in string if c not in ',.!?']
print(''.join(new).lower())
