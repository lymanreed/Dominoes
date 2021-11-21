text = input().split()
for i in range(1, len(text)):
    text[i] = text[i].capitalize()
print("".join(text))
