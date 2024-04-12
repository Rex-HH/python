n = int(input())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
m = [[0 for i in range(25)]for j in range(25)]
ans = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
yes = 0

def dp(x, y):
    global yes, n, r, c
    if yes == 1:
        return True
    if x == n and y == n and sum(r) == 0 and sum(c) == 0:
        yes = 1
        return True
    else:
        return False

def check(x, y):
    global n, r, c,m
    if x > n or x < 1 or y > n or y < 1:
        return False
    elif m[x][y] == 1:
        return False
    elif c[x-1] < 1 or r[y-1] < 1:
        return False
    else:
        return True


def dfs(x, y):
    global yes, n, r, c, m,ans
    ans.append(((x - 1) * n + y -1))
    if dp(x, y):
        return 
    for i in range(4):
        if check(x+dx[i], y+dy[i]):
            m[x+dx[i]][y+dy[i]] = 1
            #print(m)
            c[x+dx[i]-1] -= 1
            r[y+dy[i]-1] -= 1
            #print(c)
            #print(r)
            dfs(x+dx[i], y+dy[i])
            m[x+dx[i]][y+dy[i]] = 0
            c[x+dx[i]-1] += 1
            r[y+dy[i]-1] += 1
        if yes == 1:
            return
    ans.pop()
    return
m[1][1] = 1
c[0] -= 1
r[0] -= 1
dfs(1, 1)
for i in ans:
    print(i, end=' ')
#print(ans)
                   
