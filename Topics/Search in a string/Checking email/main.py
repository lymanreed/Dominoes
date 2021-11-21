def check_email(string):
    if " " in string:
        return False

    if string.count("@") != 1:
        return False

    at_index = string.find("@")
    if at_index in (0, len(string) - 1):
        return False

    dot_index = string.find(".", at_index + 1)
    if dot_index in (-1, len(string) - 1, at_index + 1):
        return False

    return True
