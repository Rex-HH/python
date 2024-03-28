import os
import sys

h = []
w = []


n, k = map(int, input().split())
for _ in range(n):
    _input = list(map(int, input().split()))
    h.append(_input[0])
    w.append(_input[1])

def pd(x):

    _sum = 0
    for i in range(n):
        _sum += (h[i] // x) * (w[i] // x)

    if _sum < k:
        return False
    else:
        return True

hight = max(h)
wight = max(w)
high = max(hight, wight)
low = 1

while low < high:

    mid = (low + high + 1) // 2
    if pd(mid):
        low = mid

    else:
       high = mid - 1
    #print(low, high)

print(low)
    
    
