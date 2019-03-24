def same_chars(str_1, str_2):
    if (len(str_1) != len(str_2)):
        return False
    dict_1 = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
        "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
        "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
        "y": 0, "z": 0,
    }

    dict_2 = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
        "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
        "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
        "y": 0, "z": 0,
    }

    for i in str_1:
        if(i in dict_1):
            dict_1[i] += 1

    for i in str_2:
        if(i in dict_2):
            dict_2[i] += 1

    if (dict_1 == dict_2):
        return True
    else:
        return False

print(same_chars("taha ", "taha "))
