try:
    print(email[:email.index("@")])
except ValueError:
    print("Invalid email address")
