def choose_vowels(letters):
    vowels = ['a', 'e', 'i', 'u', 'o']
    return list(filter(lambda l: l in vowels, letters))
