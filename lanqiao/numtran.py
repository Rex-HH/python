a = [[0] * 101] * 101
n = int(input())
for i in range(1, n+1):
    a[i] = list(map(int, input().split()))

for i in range(n -1 , 0, -1):
    for j in range(0, i):
        if a[i + 1][j] > a[i + 1][j + 1]:
            a[i][j] += a[i + 1][j]
        else:
            a[i][j] += a[i + 1][j + 1]
print(a[1][0])
