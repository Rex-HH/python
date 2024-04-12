t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    if x > n/2:
        print("YES")
    else:
        print("NO")
