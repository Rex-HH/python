
# 请在此输入您的代码
from queue import Queue

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 两两组合形成上下左右四个方向
#      1------------------> x
#      |
#      |
#      |
#      |
#      |
#      |
#      |
#      ↓
#      y

# dx[0]=0 dy[0]=1 那么代表向下的方向
# dx[1]=1 dy[1]=0 那么代表向右的方向
# dx[2]=-1 dy[0]=0 那么代表向左的方向
# dx[3]=0 dy[1]=-1 那么代表向上的方向

Map = []

q = []
qfront = 0
qend = 0

n = 0
m = 0
k = 0

length = 0


def pd(x, y):
    if x < 0:
        return False
    # x 轴坐标左侧越界
    elif x >= n:
        return False
    # x 轴坐标右侧越界
    elif y < 0:
        return False
    # y轴坐标上侧越界
    elif y >= m:
        return False
    # y 轴坐标下侧越界
    elif Map[x][y] == 'g':
        return False
    # 已经长草了
    else:
        return True
    # 在范围内，且没长草


def BFS():
    global k, q, n, m, Map, length, qend, qfront
    # print("K Length", k, length)
    while k > 0 and length > 0:
        tempPair = q[qfront]
        qfront += 1
        x = tempPair[0]  # 横坐标
        y = tempPair[1]  # 纵坐标
        for i in range(4):

            nowx = x + dx[i]  # 扩展后的横坐标
            nowy = y + dy[i]  # 扩展后的纵坐标

            if (pd(nowx, nowy)):
                q.append((nowx,nowy))
                qend += 1
                Map[nowx][nowy] = 'g'
        length -= 1
        if length == 0:
            k -= 1
            length = qend - qfront


if __name__ == '__main__':

    n, m = map(int, input().split())
    Map = [[0 for _ in range(m)] for _ in range(n)]  # Python 动态开数组会减少运行时间

    for i in range(n):
        input_ = input()
        for j in range(m):
            Map[i][j] = input_[j]
            if Map[i][j] == 'g':
                q.append((i,j))
                qend += 1

    k = int(input())
    length = qend - qfront
    BFS()
    for i in range(n):
        str_temp = ''
        for j in range(m):
            str_temp += Map[i][j]
        print(str_temp)
