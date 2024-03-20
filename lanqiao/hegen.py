m , n = map(int, input().split())

fa = [i for i in range(m*n + 50)]
sz = [1 for _ in range(m*n + 50)]

k = int(input())

def find(x):
    
    if fa[x] == x:
        return x

    else:
        fa[x] = find(fa[x])
        return fa[x]

def merge(a, b):

    x, y = find(a), find(b)

    if sz[x] > sz[y]:
        fa[y] = x
        sz[x] += sz[y]

    else:
        fa[x] = y
        sz[y] += sz[x]

for _ in range(k):

    a, b = map(int, input().split())
    merge(a, b)

ans = 0

for i in range(1, m*n+1):
    if fa[i] == i:
        ans += 1

print(ans)    
    
