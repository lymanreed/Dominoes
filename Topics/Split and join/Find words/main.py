line = input().split()
words = [word for word in line if word.endswith("s")]
print("_".join(words))
