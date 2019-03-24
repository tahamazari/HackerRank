def palindrome(string):
    i = 0
    j = len(string) - 1

    while i != len(string) and j != -1:
        print(string[i], string[j])
        if(string[i] != string[j]):
            return False
        else:
            i += 1
            j -= 1

    return True

print(palindrome("AlkalA"))
