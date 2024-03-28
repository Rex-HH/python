import sys
dp = [0] * (20 + 5)
dp[2] = 1
for i in range(3, 21):
    dp[i] = (i - 1) * (dp[i-2] + dp[i-1])

for i in sys.stdin:
    print(dp[int(i)])

