def ducth_flag(arr, piv):
    pivot = arr[piv]
    iter = 0

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[j] < pivot):
                arr[i], arr[j] = arr[j], arr[i]
                break

    for i in reversed(range(len(arr))):
        if arr[i] < pivot:
            break
        for j in reversed(range(i)):
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
    return arr

print(ducth_flag([0,2,3,1,1], 2))
