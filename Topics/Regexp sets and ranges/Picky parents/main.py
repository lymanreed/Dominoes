import re

name = input()
template = '[B-N][aeiou]'
if re.match(template, name):
    print('Suitable!')
