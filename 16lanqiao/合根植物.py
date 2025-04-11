m, n = map(int, input().split())

fa = [i for i in range(m * n + 1)]
sz = [1 for _ in range(m * n + 1)]


def find(x):

    if fa[x] == x:
        return x
    else:
        fa[x] = find(fa[x])
        return fa[x]


def merge(x, y):
    xx, yy = find(x), find(y)
    if xx == yy:
        return

    if sz[xx] > sz[yy]:
        fa[yy] = xx
    else:
        fa[xx] = yy


k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    merge(a, b)


ans = set()

for i in range(1, m*n+1):
    ans.add(find(i))

print(len(ans))
    


