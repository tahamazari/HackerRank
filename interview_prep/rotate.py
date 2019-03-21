def rotate(arr, n):
    temp = arr[0:n+1]
    arr = arr[n+1:len(arr)]
    for i in range(0, len(temp)):
        arr.append(temp[i])
    return arr

print(rotate([0,1,2,3,4], 2))
