

dx = [0, 1, -1, 0]

dy = [1, 0, 0, -1]

G = []

Vis = []

# --------队列模拟-----------
q = []                   # |
                         # |
qfront = 0               # |
                         # |
qend = 0                 # |
# --------队列模拟-----------


n = 0
m = 0
ans = 0

startX=0
startY=0

endX=0
endY=0

def pd(x, y):
    if x < 1:
        return False

    # x 轴坐标左侧越界

    elif x > n:
        return False
    # x 轴坐标右侧越界

    elif y < 1:
        return False
    # y轴坐标上侧越界

    elif y > m:
        return False
    # y 轴坐标下侧越界

    elif Vis[x][y]!=0:
        return False
    #已经访问了
    elif G[x][y] != '1':
        return False
    # 已经访问了
    else:
        return True

    # 在范围内，且没长草

def check( x,  y):

    global ans
    if x == endX and y == endY :  #找到终点，把距离给他

        ans  =  Vis[x][y];

        return True;

    else   :
        return False;

def BFS():


    global qend ,qfront

    q.append((startX,startY))

    qend+=1

    Vis[startX][startY]=1

    while qend-qfront!=0:

        tempPair = q[qfront]
        qfront+=1

        x = tempPair[0]  # 横坐标

        y = tempPair[1]  # 纵坐标
        if check(x,y):
            return

        for i in range(4):

            nowx = x + dx[i]  # 扩展后的横坐标

            nowy = y + dy[i]  # 扩展后的纵坐标

            if (pd(nowx, nowy)):

                q.append((nowx,nowy))
                qend+=1

                Vis[nowx][nowy] = Vis[x][ y] + 1


if __name__ == '__main__':

    n, m = map(int, input().split())

    G = [[0 for _ in range(m+10)] for _ in range(n+10)]  # Python 动态开数组会减少运行时间

    Vis = [[0 for _ in range(m+10)] for _ in range(n+10)]  # Python 动态开数组会减少运行时间

    for i in range(n):
        input_ = input().split()
        for j in range(m):
            G[i+1][j+1] = input_[j]

    startX ,startY , endX ,endY = map(int, input().split())

    BFS()

    print(ans-1)

