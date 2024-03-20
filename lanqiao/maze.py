n, m = map(int, input().split())
maze = [[0 for _ in range(m+10)] for _ in range(n+10)]
Vis = [[0 for _ in range(m+10)] for _ in range(n+10)]
for i in range(n):
    input_ = list(map(int,input().split()))
    for j in range(m):
        maze[i][j] = input_[j]
    #maze.append(list(map(int, input().split())))
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
que = [(x1, y1)]
#step = 0
qnow = 0
qend = 0
ans = 0
#lg = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check(x, y):
    global ans
    if x == x2 and y == y2:
        ans = Vis[x][y]
        #print(Vis[y][x])
        return True
    else:
        return False
def dp(x, y):
    global m, n, maze
    if x >= n or y >= m or x < 0 or y < 0 or \
    maze[x][y] != 1 or Vis[x][y] != 0:
        return False
    else:
        return True
def BFS():
    global maze, x2, y2, que, step, qnow, lg, dx, dy,qend
    qend += 1
    Vis[x1][y1] = 1
    while qend - qnow != 0:
        x, y = que[qnow]
        qnow += 1
        if check(x, y):
            return
        for i in range(4):
            x3, y3 = x + dx[i], y + dy[i]
            if dp(x3, y3):
                que.append((x3, y3))
                #print(x3, y3)
                qend += 1
                Vis[x3][y3] = Vis[x][y] + 1
                #print(Vis[y3][x3])

BFS()
print(ans - 1)
