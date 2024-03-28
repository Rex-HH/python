import os
import sys

esp = 1e-9

n, m = map(int, input().split())

low = 0
high = n

def pd(x):

    _pow = 1
    for _ in range(m):
        _pow *= x

    if _pow < n:
        return True
    
    else:
        return False

while (high - low) > esp:

    mid = (low + high) / 2

    if pd(mid):
        low = mid

    else:
        high = mid

print("%.7f" % low)
