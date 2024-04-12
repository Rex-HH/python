n = int(input())

for i in range(1, n+1):
    ans = 0
    ans = max(ans, 2 * (i-1))
    ans = max(ans, 2 * (n-i))
    print(ans)
