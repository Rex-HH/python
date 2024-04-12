n, m = map(int, input().split())

a = [0] + list(map(int, input().split()))
p = list(map(int, input().split()))
dp = [False] * (n + 1)
for i in p:
    dp[i] = True

flag = True
for i in range(n - 1):
    for j in range(1, n - i):
        if a[j] > a[j+1]:
            if dp[j]:
                a[j], a[j+1] = a[j+1], a[j]
            else:
                print("NO")
                flag = False
        if not flag:
            break
    if not flag:
        break

if flag:
    print("YES")


        
