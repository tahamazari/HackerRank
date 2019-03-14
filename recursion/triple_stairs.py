

def stairs(num):
    if num < 0:
        return 0
    elif num == 0:
        return 1
    else:
        return stairs(num - 1) + stairs(num - 2) + stairs(num - 3)


print(stairs(50))
