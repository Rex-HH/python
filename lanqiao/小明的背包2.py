n, v = map(int, input().split())

a = [[0, 0]]

dp = [[0 for i in range(v + 1)] for j in range(n + 1)]

for _ in range(n):
    a.append(list(map(int, input().split())))
    

for k in range(1, n + 1):
    for y in range(1, v + 1):
        if a[k][0] <= y:
            dp[k][y] = max(dp[k-1][y], dp[k][y-a[k][0]] + a[k][1])

        else:   
            dp[k][y] = dp[k-1][y]

#print(dp)

print(dp[n][v])
