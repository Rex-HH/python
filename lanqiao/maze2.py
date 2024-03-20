maze = []
road = []

input_ = input()

while input_ != "":
    
    maze.append(list(input_))
    input_ = input()

n, m = len(maze)-1, len(maze[0])-1
print(n, m)

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]
uxy = ["D", "L", "R", "U"]

q = []
qnow = 0

def check(x, y):
    #print(x, y, sep=",")
    if x == m and y == n:
        print("1")
        return True
    else:
        return False

def dp(x, y):
    global maze
    if y > n or x > m or x < 0 or y < 0 or maze[y][x] == "1":
        return False
    else:
        maze[y][x] = '1'
        return True

def BFS():

    global q, road, qnow

    q.append((0,0))
    road.append([-1, "S"])

    while True:
    
        x, y = q[qnow]
       # print(len(q))
       # print(qnow)
        
        if check(x, y):
            return

        
        
        for i in range(4):

            x2, y2 = x + dx[i] , y + dy[i]

            if dp(x2, y2):
                q.append((x2, y2))
                road.append([qnow, uxy[i]])

        qnow += 1

BFS()

ans = []

while qnow != 0:
    ans.append(road[qnow][1])
    qnow = road[qnow][0]

for i in range(len(ans)):
    print(ans.pop(), end="")
        

            
    
        

    
