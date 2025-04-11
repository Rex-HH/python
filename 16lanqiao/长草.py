n, m = map(int, input().split())

maze = [[] for _ in range(n)]

for i in range(n):
    maze[i] = list(input())

z = int(input())
q = [[] for _ in range(z+1)]
#print(q)

for i in range(n):
    
    #print(maze[i])
    for j in range(m):
        #print(maze[i][j])
        if maze[i][j] == 'g':
            q[0].append((i, j))
#print(q)


move  = [-1, 0, 1, 0, -1]
for k in range(z):
    l = 0
    while True:
        #print(q[k+1])
        cur = q[k][l]
        x, y = cur[0], cur[1]
        for i in range(4):
            xx, yy = x + move[i], y + move[i+1]

            if xx < 0 or xx >= n or yy < 0 or yy >= m or maze[xx][yy] == 'g':
                continue
            else:
                maze[xx][yy] = 'g'
                q[k+1].append((xx, yy))

        l += 1
        if l >= len(q[k]):
           
            break
for i in range(n):
    print(''.join(maze[i]))
#print(maze)
        
        
    
