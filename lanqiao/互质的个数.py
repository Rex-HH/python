t = int(input())

for _ in range(t):

    n, m, k = map(int, input().split())

    l, r = k, k
    cnt = 1
    ans = 1
    while r*m + 1 <=n:
        r = r * m + 1
        l = l * m - m + 2
        cnt *= m
        ans += cnt
    if r * m + 1 > n:
        l = l * m - m + 2
        ans += max(0, n - l + 1)
    print(ans)
