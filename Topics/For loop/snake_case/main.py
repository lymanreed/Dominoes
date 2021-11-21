word = input()
new_word = ''
for letter in word:
    if letter.isupper():
        new_word += f'_{letter.lower()}'
    else:
        new_word += letter.lower()
print(new_word.strip('_'))
