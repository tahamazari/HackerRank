# def rotate(arr, n):
#     temp = arr[0:n+1]
#     arr = arr[n+1:len(arr)]
#     for i in range(0, len(temp)):
#         arr.append(temp[i])
#     return arr

def rotate(arr, n):
    temp = []
    for i in range(0, len(arr)):
        if i - n < 0:
            temp.append(arr[len(arr)-(n-i)])
        else:
            temp.append(arr[i-n])
    return temp

print(rotate([0,1,2,3,4], 3))
