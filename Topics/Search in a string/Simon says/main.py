def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        action = instructions[len("Simon says "):]
    elif instructions.endswith("Simon says"):
        action = instructions[:len(" Simon says") + 1]
    else:
        action = "won't do it!"
    return "I " + action
