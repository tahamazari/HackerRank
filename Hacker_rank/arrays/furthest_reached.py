def array_advance(arr):
    furthest_reached = 0
    last = len(arr) - 1
    i = 0

    while i <= furthest_reached and furthest_reached < last:
        furthest_reached = max(furthest_reached, arr[i] + i)
        i += 1

    if(furthest_reached >= last):
        print("true")
    else:
        print("false")
        
    return furthest_reached >= last

array_advance([3, 3, 2, 0, 1, 1, 1])
