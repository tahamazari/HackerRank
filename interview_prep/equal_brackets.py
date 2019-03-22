def equal(val):
    if len(val)%2 !=0:
        return False
    indece = int(len(val)/2)
    temp_1 = [val[0:int(len(val)/2)]]
    temp_2 = [val[int(len(val)/2):len(val)]]

    i = 0
    j = len(temp_2)

    while i != (j-1):
        if((temp_1[i] == "[" and temp_2[j] == "]") or (temp_1[i] == "(" and temp_2[j] == ")") or (temp_1[i] == "{" and temp_2[j] == "}")):
            i += 1
            j -= 1
        else: break

equal("{{[]}}")
