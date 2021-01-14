def csFindAddedLetter(str_1, str_2):
    s1 = {}
    for char in str_1:
        if char in s1.keys():
            s1[char] = s1[char] + 1
        else:
            s1[char] = 1
    for char in str_2:
        if char not in s1.keys():
            return char
        else:
            s1[char] = s1[char] -1
            if s1[char] < 0:
                return char
    

