def csFirstUniqueChar(input_str):
    for i, char in enumerate(input_str):
        if input_str.count(char) == 1:
            return i
    return -1

