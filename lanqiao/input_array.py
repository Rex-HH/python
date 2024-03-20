maxn = 2000000
fa = [i for i in range(maxn)]

n = int(input())

a = list(map(int, input().split()))

def find(x):

    if fa[x] == x:
        return x

    else:
        fa[x] = find(fa[x])
        return fa[x]

def merge(a, b):

    x, y = find(a), find(b)
    fa[x] = y

for i in range(n):
    
    t = find(a[i])
    
    print(t, end = ' ')
    
    merge(t, t+1)
    
