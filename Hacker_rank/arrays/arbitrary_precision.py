def precision(arr):
    string = ""
    arr_str = []

    for i in arr:
        string += str(i)

    string = int(string) + 1
    string = str(string)

    for i in string:
        arr_str.append(i)

    print(string, arr_str)

arr = [1, 5, 1]

precision(arr)
