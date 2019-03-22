def is_rotation(string_1, string_2):
    temp_string = string_1 + string_1
    if string_2 in temp_string:
        return True
    else:
        return False

print(is_rotation('Taha', 'ahaT'))
