n = int(input())

INF = int(-0x3f3f3f3f)

sum = 0
maze = [INF] * n


def check(level):
    global sum
    if level == n:
        sum += 1
        return True
    else:
        return False

def pd(i, level):
    for l in range(level):
        if abs(i - maze[l]) == abs(level - l) or i == maze[l]:
            return False
    return True

def dfs(level):
    if check(level):
        return 
    global sum
    for i in range(n):
        if pd(i, level):
            maze[level] = i
            dfs(level + 1)
            maze[level] = INF

dfs(0)
print(sum)
            
        
        
