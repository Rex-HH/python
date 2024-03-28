INF = 0x3f3f3f3f3f3f3f3f

n, m = map(int,input().split())

dis = [[INF for i in range(n+1)] for j in range(n+1)]

c = [[] for i in range(n-1)]
for i in range(n+1):
    dis[i][i] = 0

for i in range(n-1):
    x, y = map(int, input().split())
    dis[x][x] += 1
    dis[y][y] += 1
    c[i] = (x, y)

for x, y in c:
    dis[x][y] = dis[y][x] = dis[x][x] + dis[y][y]

for k in range(1, n+1):
    for i in range(1, n):
        for j in range(i+1, n+1):
            dis[j][i] = dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j] - dis[k][k])

for i in range(m):
    x, y = map(int, input().split())
    print(dis[x][y])
