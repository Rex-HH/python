n, m = map(int, input().split())

fa = [i for i in range(n + 1)]
sz = [1] * (n + 1)

def find(x):
    global fa
    
    if fa[x] == x:
        return x

    fa[x] = find(fa[x])
    
    return fa[x]

def merge(a, b):
    global sz, fa
    
    aa = find(a)
    bb = find(b)

    if sz[aa] > sz[bb]:
        fa[bb] = aa
        sz[aa] += sz[bb]
    else:
        fa[aa] = bb
        sz[bb] += sz[aa]


for _ in range(m):
    op, x, y = map(int, input().split())

    if op == 1:
        merge(x, y)
    else:
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")
