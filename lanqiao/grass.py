n, m = map(int, input().split())
gi = [[0 for _ in range(m)] for _ in range(n)]
que = []
lg = 0
for i in range(n):
    input_ = input()
    for j in range(m):
        gi[i][j] = input_[j]
        if gi[i][j] == 'g':
            que.append((i,j))
            lg += 1
k = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dp(x, y):
    if x < 0 or x >= m or y < 0 or y >= n or gi[y][x] == 'g':
        return False
    else:
        return True
qnow = 0
def BFS():
    global k, dx, dy, lg, que,gi, qnow
    while k > 0:
        for i in range(lg):
            for j in range(4):
                y, x = que[qnow]
                if dp(x + dx[j], y + dy[j]):
                    gi[y + dy[j]][x + dx[j]] = 'g'
                    que.append((y + dy[j],x + dx[j]))
            qnow += 1
        k -= 1
        lg = len(que) - qnow
BFS()
for i in range(n):
    for j in range(m):
        print(gi[i][j], end='')
    print()
                
