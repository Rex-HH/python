import os
import sys
import math

class Edge:

    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

m = int(input())
jmp = list(map(int, input().split()))
n = int(input())
fa = [i for i in range(n+1)]
sz = [1 for _ in range(n+1)]
x = [0 for _ in range(n+1)]
y = [0 for _ in range(n+1)]
for i in range(1, n+1):
    x[i], y[i] = map(int, input().split())
    
e = []

def find(x):

    if fa[x] == x:
        return fa[x]
    else:
        fa[x] = find(fa[x])
        return fa[x]

def merge(a, b):
    
    aa = find(a)
    bb = find(b)
    
    if aa != bb:
        if sz[aa] > sz[bb]:
            fa[bb] = aa
            sz[aa] += sz[bb]

        else:
            fa[aa] = bb
            sz[bb] + sz[aa]


for i in range(1, n+1):
    for j in range(i+1, n+1):
        dis = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
        e.append(Edge(i, j, dis))

e.sort(key=lambda x: x.w)

maxdis = 0
num = 0
for u in e:
    
    if find(u.a) != find(u.b):
        merge(u.a, u.b)
        maxdis = max(maxdis, u.w)
        num += 1
        if num == n-1:
            break
        
ans = 0
for i in jmp:
    if i >= maxdis:
        ans += 1

print(ans)
