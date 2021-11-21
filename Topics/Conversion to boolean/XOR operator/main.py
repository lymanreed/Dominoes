def xor(a, b):
    if a and b or bool(a) is False and bool(b) is False:
        return False
    return a if a else b
