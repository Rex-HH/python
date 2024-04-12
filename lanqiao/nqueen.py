N = int(input())
ans = 0
a = [0 for i in range(15)]

def check(r, i):
    for j in range(1, r):
        if a[j] == i:
            return False
        elif (r - j) == abs(i - a[j]):
            return False
    return True
    

def dfs(r):
    global ans, a, N
    if r > N:
        ans += 1
        return
    for i in range(1, N+1):
        if check(r, i):
            a[r] = i
            dfs(r + 1)
        else:
            continue
dfs(1)
print(ans)
            
    
