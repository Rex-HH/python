n, k = map(int, input().split())
dp = [[0 for j in range(k + 5)] for i in range(n + 5)]
for i in range(1, n + 1):
    dp[i][1] = 1
    dp[i][i] = 1
for i in range(3, n + 1):
    for j in range(2, k + 1):
        if i > j:
            dp[i][j] = dp[i-1][j-1] + dp[i-j][j]
print(dp[n][k])
