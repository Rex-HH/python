import sys
import os
import math

def caculate(xi, yi, hi, xj, yj, hj):
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2) + (hi - hj) ** 2

def find(x):
    if x != fa[x]:
        fa[x] = find(fa[x])
    return fa[x]

def kruskal():
    global fa
    e.sort(key=lambda x: x[2])
    fa = list(range(n+1))
    ans = 0
    cnt = 0
    for a, b, w in e:
        aa = find(a)
        bb = find(b)
        if aa != bb:
            fa[aa] = bb
            ans += w
            cnt += 1
            if cnt == n-1:
                return ans

n = int(input())
d = [[] for _ in range(n+1)]

for i in range(1, n+1):
    d[i] = tuple(map(int, input().split()))
    
e = []
for i in range(1, n):
    for j in range(i+1, n+1):
        xi, yi, hi = d[i]
        xj, yj, hj = d[j]
        e.append((i, j, caculate(xi, yi, hi, xj, yj, hj)))
        
print(round(kruskal(), 2))


       
