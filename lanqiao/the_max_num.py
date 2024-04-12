n, a, b = map(int, input().split())
ln = [int(i) for i in str(n)]
buflist = []
maxnum = 0
def check(x, y):
    if x >= y:
        return True
    else:
        return False
def dfs(x):
    global ln, a, b,buflist, maxnum
    if x >= len(ln):
        strlist = list(map(str, buflist))
       # print(strlist)
        sumstr = ""
        for i in strlist:
            sumstr += i
        sumint = int(sumstr)
       # print(sumint)
        if sumint > maxnum:
            maxnum = sumint
        return
    if check(a, (9-ln[x])) or check(b, (ln[x]+1)):
        if check(a, (9-ln[x])):
            a -= (9-ln[x])
            buflist.append(9)
          #  print(a,b)
            dfs(x + 1)
            buflist.pop()
            a += (9-ln[x])
        if check(b, (ln[x]+1)):
            b -= (ln[x]+1)
            buflist.append(9)
            #print(a,b)
            dfs(x + 1)
            buflist.pop()
            b += (ln[x]+1)
    elif check(a, 1):
        buflist.append(ln[x]+a)
       # print(buflist)
        c = a
        a = 0
        dfs(x + 1)
        a = c
        buflist.pop()
    else:
        buflist.append(ln[x])
        dfs(x + 1)
        buflist.pop()
dfs(0)
print(maxnum)
    
