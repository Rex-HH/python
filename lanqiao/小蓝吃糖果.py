n = int(input())

m = list(map(int, input().split()))

if max(m) - 1 > sum(m) - max(m):
    print("No")

else:
    print("Yes")
