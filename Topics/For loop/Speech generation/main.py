digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
phone_number = input()
for digit in phone_number:
    print(digits[int(digit)])
