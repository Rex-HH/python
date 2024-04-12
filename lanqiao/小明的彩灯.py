n, q = map(int, input().split())
a = [0] + list(map(int, input().split())) + [0]


for i in range(n, 0, -1):
    a[i] = a[i] - a[i-1]


for _ in range(q):
    l, r, x = map(int, input().split())
    a[l] += x
    a[r+1] -= x

for i in range(1, n + 1):
    a[i] = a[i] + a[i-1]

for i in range(1, n + 1):
    print(a[i] if a[i] >= 0 else 0, end=' ')


