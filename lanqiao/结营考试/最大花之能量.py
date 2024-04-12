n = int(input())

a = [0] + list(map(int, input().split()))

g = [0] * (n + 1)

ans = 0
for i in range(1, n + 1):
    res = 0
    for j in range(1, i):
        if a[j] < a[i] and g[j] > res:
            res = g[j]

    g[i] = res + a[i]
    if g[i] > ans:
        ans = g[i]

print(ans)


    
