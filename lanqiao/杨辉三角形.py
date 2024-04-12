n = int(input())

def C(a, b):
    res = 1
    i = a
    j = 1

    while j <= b:
        res = res * i // j
        if res > n:
            return int(res)

        i -= 1
        j += 1

    return int(res)


for i in range(16, -1, -1):
    flag = False
    l = 2 * i
    r = max(n, l)
    mid = (l + r) // 2

    while l <= r:
        
        mid = (l + r) // 2
        c = C(mid, i)
        if c > n:
            r = mid - 1
        elif c == n:
            flag = True
            break
        else:
            l = mid + 1

    if flag:
        print((1 + mid) * mid // 2 + i + 1)
        break
        
