import sys
import os

t = int(input())

for _ in range(t):

    n = int(input())
    m = [0] * 205

    for i in range(n):

        s, t = map(int, input().split())
        s = (s + 1) // 2
        t = (t + 1) // 2
        low, high = min(s, t), max(s, t)

        m[low] += 1
        m[high+1] -= 1

    for j in range(1, 205):
        m[j] = m[j] + m[j-1]
        
    print(max(m) * 10)
