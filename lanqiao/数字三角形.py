n = int(input())

dp = [[] for _ in range(n+5)]
b = []
for _ in range(n):
    b.append(list(map(int, input().split())))

dp[0].append(b[0][0]) 

for i in range(1, n):
    for j in range(i + 1):

        if j == 0:
            dp[i].append(dp[i-1][j] + b[i][j])

        elif j == i:
            dp[i].append(dp[i-1][j-1] + b[i][j])

        else:
            dp[i].append(max(dp[i-1][j-1] + b[i][j], dp[i-1][j] + b[i][j]))
   # print(dp[i])
if n & 1:
    print(dp[n-1][n//2])

else:
    print(max(dp[n-1][n//2], dp[n-1][n//2 - 1]))

#print(dp)
