string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0
for letter in string:
    if letter in vowels:
        count += 1
print(count)
