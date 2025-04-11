



n, m = map(int, input().split())
cf = [0] * (n + 1)
for _ in range(m):
    l, r, cost = map(int, input().split())
    cf[l] += cost
    cf[r + 1] -= cost

ans = cf[0]
for i in range(1, n):
    cf[i] += cf[i - 1]
    ans += cf[i]

print(ans)
