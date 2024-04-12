n, m = map(int, input().split())
ans = 0

for _ in range(m):
    l, r, s, e = map(int ,input().split())

    ans += (s + e) * (r - l + 1) // 2

print(ans)
    

'''n, m = map(int, input().split())
dp = [0] * (n + 3)

for _ in range(m):

    l, r, s, e = map(int, input().split())
    #print(l, r, s, e)
    d = e - s
    if d == 0:
        dp[l] += s
        dp[l+1] -= s
        dp[r+1] -= s
        dp[r+2] += s
    else:
        d /= (r - l)
        dp[l] += d
        dp[r+1] -= d
        dp[r+1] -= e
        dp[r+2] += e
    #print(dp)
       
#print(dp)
for i in range(1, n + 1):
    dp[i] += dp[i-1]
#print(dp)
ans = 0
for i in range(1, n + 1):
    dp[i] += dp[i-1]
    ans += dp[i]

#print(dp)
print(ans)    
'''
