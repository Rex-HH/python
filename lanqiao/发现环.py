n = int(input())

e = [[] for _ in range(n+1)]
vis = [False] * (n + 1)
ring = []
pre = [0] * (n + 1)

for _ in range(n):
    a, b = map(int, input().split())

    e[a].append(b)
    e[b].append(a)

def dfs(x, fa):
    global ring, pre, vis
    for son in e[x]:
        if len(ring) > 0: return
        if not vis[son]:
            vis[son] = True
            pre[son] = x
            dfs(son, x)

        elif son != fa:
            temp = x
            while temp != son:
                ring.append(temp)
                temp = pre[temp]

            ring.append(son)
            return
dfs(1,0)
ring.sort()
for i in ring:
    print(i, end=' ')
    
    
