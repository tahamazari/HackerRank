

def myfunc(n):
    yip = 0
    yip += 1
    print(yip)
    if (n==1):
        return
    elif n > 10:
        return myfunc(n - 4)
    elif n > 5:
        return myfunc(n - 2)
    else:
        return myfunc(n - 1)

print(myfunc(25))
