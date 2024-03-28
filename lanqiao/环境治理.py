import copy
d = []
l = []
n, q = map(int, input().split())

for _ in range(n):
    d.append(list(map(int, input().split())))

for _ in range(n):
    l.append(list(map(int, input().split())))

f = copy.deepcopy(l)

def floyd(f):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                f[i][j] = min(f[i][j], f[i][k] + f[k][j])
    p = 0
    for i in range(n):
        for j in range(n):
            p += f[i][j]
    #print(p)
    return p

def check(mid):
    global f
    f = copy.deepcopy(d)
    h = mid//n
    m = mid%n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if i < m:
                f[i][j] = max(l[i][j], f[i][j] - h -1)
            else:
                f[i][j] = max(l[i][j], f[i][j] - h)
            f[j][i] = f[i][j]
    return floyd(f) <= q

def solve():
    if floyd(f) > q:
        print(-1)
        return 
    low, high = 0, 10000000
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1

        #print(low, mid, high)
    print(low)
    return

solve()
        

