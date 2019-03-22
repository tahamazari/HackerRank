def largest(arr):
    hashed_array = [0]*10
    sorted_array = []
    number = ''

    for i in range(0, len(arr)):
        hashed_array[arr[i]] = hashed_array[arr[i]] +  1

    for i in range(0, len(hashed_array)):
        if(hashed_array[i] == 0):
            pass
        else:
            j = 0
            while j < hashed_array[i]:
                sorted_array.append(i)
                j += 1

    for i in reversed(range(len(arr))):
        number += str(sorted_array[i])

    return number

print(largest([8,2,1,4]))
