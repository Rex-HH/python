n = int(input())
a = [0 for i in range(1005)]
def getnum(n):
    global a
    ans = 0
    for i in range(n // 2, 0, -1):
        if a[i] != 0:
            ans += a[i]
        else:
            a[i] = getnum(i)
            ans += a[i]
    return ans + 1

print(getnum(n))
