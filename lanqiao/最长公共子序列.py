n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#print(dp)

print(dp[n][m])
