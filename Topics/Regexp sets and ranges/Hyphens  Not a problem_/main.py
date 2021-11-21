import re

# your code here
word = input()
print(bool(re.match('[a-zA-Z]+-[a-zA-Z]', word)))
