n = int(input())
a = [0] + list(map(int, input().split()))
r = (n + 1) // 2

for i in range(1, r + 1):
    if a[i] > a[n+1-i]:
        a[i], a[n+1-i] = a[n+1-i], a[i]

flag = True
for i in range(1, n):
    if a[i] > a[i+1]:
        print("NO")
        flag = False
        break

if flag:
    print("YES")
        
