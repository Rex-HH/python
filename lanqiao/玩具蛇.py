mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

def step(box, res, now):
    if now[2] == 16:
        res += 1
       # print(res)
        return res
    for i in range(4):
        x = now[0] + mx[i]
        y = now[1] + my[i]

        if not(0 <= x <= 3 and 0 <= y <= 3) or box[x][y] > 0 : continue

        new = (x, y, now[2] + 1)
        #print(new)
        box[x][y] = new[2]
        res = step(box, res, new)
        box[x][y] = 0
    return res
def dfs(x, y):
    box = [[0 for i in range(4)] for j in range(4)]
    res = 0
    now = (x, y, 1)
    box[x][y] = now[2]
    res = step(box, res, now)
    return res

if __name__ == "__main__":
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dfs(i, j)

    print(ans)
    
